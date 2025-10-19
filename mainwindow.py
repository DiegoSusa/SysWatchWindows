import sys
import os
import time
import psutil
import pyqtgraph as pg

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableWidgetItem, QMessageBox,
    QAbstractItemView, QHeaderView
)
from PySide6.QtCore import QTimer, Qt

from ui_form import Ui_MainWindow


MB = 1024 ** 2
GB = 1024 ** 3



class NumericItem(QTableWidgetItem):
    def __init__(self, value: float, text: str | None = None):
        super().__init__(text if text is not None else f"{value}")
        self._num = float(value)

    def __lt__(self, other):
        if isinstance(other, NumericItem):
            return self._num < other._num
        try:
            return self._num < float(other.text())
        except Exception:
            return super().__lt__(other)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        try:
            self.ui.SpinIntervalo.setRange(100, 10000)
            if self.ui.SpinIntervalo.value() < 100:
                self.ui.SpinIntervalo.setValue(1000)  
        except Exception:
            pass
        try:
            self.ui.SpinCantidad.setRange(1, 200)
            if self.ui.SpinCantidad.value() < 5:
                self.ui.SpinCantidad.setValue(20)    
        except Exception:
            pass

        for w in (self.ui.graphic1, self.ui.graphic2, self.ui.graphic3):
            w.setBackground('#26253a')
            w.getAxis("left").setPen("#f0f0f0")
            w.getAxis("bottom").setPen("#f0f0f0")
            w.showGrid(x=True, y=True, alpha=0.2)
            w.setYRange(0, 100)  
            w.setXRange(0, 60)

        self.ui.progressBarCPU.setRange(0, 100)
        self.ui.progressBarMem.setRange(0, 100)
        self.ui.progressBarDisc.setRange(0, 100)

        self.win_len = 60
        self.x_vals  = list(range(self.win_len))
        self.cpu_vals = [0.0] * self.win_len
        self.mem_vals = [0.0] * self.win_len
        self.dsk_vals = [0.0] * self.win_len

        self.cpu_curve = self.ui.graphic1.plot(self.x_vals, self.cpu_vals, pen=pg.mkPen("#ff4fa0", width=2))
        self.mem_curve = self.ui.graphic2.plot(self.x_vals, self.mem_vals, pen=pg.mkPen("#00ff85", width=2))
        self.dsk_curve = self.ui.graphic3.plot(self.x_vals, self.dsk_vals, pen=pg.mkPen("#3a7dff", width=2))

        self.table = self.ui.tableProcesos
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["PID", "NOMBRE", "CPU %", "RAM (MB)"])
        self.table.setSortingEnabled(True) 
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setWordWrap(False)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table.verticalHeader().setDefaultSectionSize(24)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 

        self.ui.LineEditFiltroNombre.textChanged.connect(self.refresh_table)
        self.ui.pushButtonRefresh.clicked.connect(self.refresh_all)
        self.ui.pushButtonKill.clicked.connect(self.kill_selected_process)
        self.ui.SpinCantidad.valueChanged.connect(lambda _: self.refresh_table())
        self.ui.SpinIntervalo.valueChanged.connect(self.update_interval)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._tick)
        self.timer.setInterval(max(100, int(self.ui.SpinIntervalo.value())))

        try:
            psutil.cpu_percent(None) 
        except Exception:
            pass

        self.proc_cache: dict[int, psutil.Process] = {}

        self.prev_disk_global = None        
        self.prev_disk_perdisk = {}        
        self.prev_disk_t = None              

        self.proc_snapshot = []

        self.timer.start()
        self.refresh_all()

    def _tick(self):
        cpu = psutil.cpu_percent(interval=None) 

        vm = psutil.virtual_memory()
        mem_percent = vm.percent

        disk_active = self._disk_active_percent()

        mount = 'C:\\' if os.name == 'nt' else '/'
        du = psutil.disk_usage(mount)
        total_gb = du.total / GB
        used_gb  = du.used  / GB
        free_gb  = du.free  / GB

        total_mem_gb = vm.total / GB
        used_mem_gb  = (vm.total - vm.available) / GB
        free_mem_gb  = vm.available / GB

        self.ui.progressBarCPU.setValue(int(cpu))
        self.ui.progressBarMem.setValue(int(mem_percent))
        self.ui.progressBarDisc.setValue(int(disk_active))

        self.cpu_vals = self.cpu_vals[1:] + [cpu]
        self.mem_vals = self.mem_vals[1:] + [mem_percent]
        self.dsk_vals = self.dsk_vals[1:] + [disk_active]
        self.cpu_curve.setData(self.x_vals, self.cpu_vals)
        self.mem_curve.setData(self.x_vals, self.mem_vals)
        self.dsk_curve.setData(self.x_vals, self.dsk_vals)

        try:
            self.ui.TotalDisc.setText(f"Total: {total_gb:.1f}GB")
            self.ui.UsadoDisc.setText(f" Usado: {used_gb:.1f}GB")
            self.ui.LibreDisc.setText(f"Libre: {free_gb:.1f}GB")
        except Exception:
            pass

        try:
            self.ui.TotalMem.setText(f"Total: {total_mem_gb:.1f}GB")
            self.ui.UsadoMem.setText(f"Usado: {used_mem_gb:.1f}GB")
            self.ui.LibreMem.setText(f"Libre: {free_mem_gb:.1f}GB")
        except Exception:
            pass

        self._update_proc_cache_and_snapshot()

        self.refresh_table()

    def _disk_active_percent(self):
        
        now = time.monotonic()

        try:
            cur = psutil.disk_io_counters() 
        except Exception:
            cur = None

        if cur is not None and hasattr(cur, "busy_time"):
            busy_ms = getattr(cur, "busy_time", None)
            if busy_ms is not None:
                if self.prev_disk_global is None or self.prev_disk_t is None:
                    self.prev_disk_global = cur
                    self.prev_disk_t = now
                    return 0.0
                dt = max(1e-3, now - self.prev_disk_t)
                dbusy = max(0.0, busy_ms - getattr(self.prev_disk_global, "busy_time", 0.0))
                self.prev_disk_global = cur
                self.prev_disk_t = now
                return max(0.0, min(100.0, (dbusy / (dt * 1000.0)) * 100.0))

        try:
            per = psutil.disk_io_counters(perdisk=True)
        except Exception:
            per = None

        if per:
            has_busy = any(hasattr(c, "busy_time") for c in per.values())
            if has_busy:
                if not self.prev_disk_perdisk or self.prev_disk_t is None:
                    self.prev_disk_perdisk = per
                    self.prev_disk_t = now
                    return 0.0
                dt = max(1e-3, now - self.prev_disk_t)
                max_percent = 0.0
                for name, curc in per.items():
                    prevc = self.prev_disk_perdisk.get(name)
                    if prevc is None:
                        continue
                    dbusy = max(0.0, getattr(curc, "busy_time", 0.0) - getattr(prevc, "busy_time", 0.0))
                    percent = (dbusy / (dt * 1000.0)) * 100.0
                    if percent > max_percent:
                        max_percent = percent
                self.prev_disk_perdisk = per
                self.prev_disk_t = now
                return max(0.0, min(100.0, max_percent))

        if cur is not None and (hasattr(cur, "read_time") or hasattr(cur, "write_time")):
            if self.prev_disk_global is None or self.prev_disk_t is None:
                self.prev_disk_global = cur
                self.prev_disk_t = now
                return 0.0
            dt = max(1e-3, now - self.prev_disk_t)
            dread = max(0.0, getattr(cur, "read_time", 0.0) - getattr(self.prev_disk_global, "read_time", 0.0))
            dwrite = max(0.0, getattr(cur, "write_time", 0.0) - getattr(self.prev_disk_global, "write_time", 0.0))
            self.prev_disk_global = cur
            self.prev_disk_t = now
            percent = ((dread + dwrite) / (dt * 1000.0)) * 100.0
            return max(0.0, min(100.0, percent))

        if per:
            if not self.prev_disk_perdisk or self.prev_disk_t is None:
                self.prev_disk_perdisk = per
                self.prev_disk_t = now
                return 0.0
            dt = max(1e-3, now - self.prev_disk_t)
            max_percent = 0.0
            for name, curc in per.items():
                prevc = self.prev_disk_perdisk.get(name)
                if prevc is None:
                    continue
                dread = max(0.0, getattr(curc, "read_time", 0.0) - getattr(prevc, "read_time", 0.0))
                dwrite = max(0.0, getattr(curc, "write_time", 0.0) - getattr(prevc, "write_time", 0.0))
                percent = ((dread + dwrite) / (dt * 1000.0)) * 100.0
                if percent > max_percent:
                    max_percent = percent
            self.prev_disk_perdisk = per
            self.prev_disk_t = now
            return max(0.0, min(100.0, max_percent))

        self.prev_disk_t = now
        return 0.0

    def _update_proc_cache_and_snapshot(self):

        current_pids = set()
        snapshot = []

        for p in psutil.process_iter(['pid', 'name']):
            pid = p.info['pid']
            name = (p.info['name'] or "")

            if pid == 0 or name.lower().strip() == "system idle process":
                continue

            current_pids.add(pid)

            proc = self.proc_cache.get(pid)
            if proc is None:
                try:
                    proc = psutil.Process(pid)
                    proc.cpu_percent(None) 
                    self.proc_cache[pid] = proc
                    cpu_val = 0.0
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    continue
            else:
                try:
                    cpu_val = proc.cpu_percent(None)  
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    continue

            try:
                mem_mb = proc.memory_info().rss / MB
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                mem_mb = 0.0

            snapshot.append({
                "pid": pid,
                "name": name,
                "cpu": float(cpu_val),
                "mem_mb": float(mem_mb),
            })

        stale = set(self.proc_cache.keys()) - current_pids
        for pid in stale:
            self.proc_cache.pop(pid, None)

        self.proc_snapshot = snapshot

    def get_process_list(self):
        filtro = self.ui.LineEditFiltroNombre.text().strip().lower()
        limite = max(1, int(self.ui.SpinCantidad.value()))

        rows = []
        for r in self.proc_snapshot:
            if filtro and filtro not in r['name'].lower():
                continue
            rows.append(r)

        rows.sort(key=lambda r: (r['cpu'], r['mem_mb']), reverse=True)

        return rows[:limite]

    def refresh_table(self):
        header = self.table.horizontalHeader()
        sort_col = header.sortIndicatorSection()
        sort_order = header.sortIndicatorOrder()

        self.table.setSortingEnabled(False)
        data = self.get_process_list()
        self.table.setRowCount(len(data))

        for r, proc in enumerate(data):
            # PID (numérico)
            item_pid = NumericItem(proc['pid'], str(proc['pid']))
            item_pid.setTextAlignment(Qt.AlignCenter)

            # NOMBRE
            item_name = QTableWidgetItem(proc['name'])
            item_name.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            # CPU %
            cpu_val = proc['cpu'] if isinstance(proc['cpu'], (int, float)) else 0.0
            item_cpu = NumericItem(cpu_val, f"{cpu_val:.1f}")
            item_cpu.setTextAlignment(Qt.AlignCenter)

            # RAM (MB)
            mem_mb = proc['mem_mb'] if isinstance(proc['mem_mb'], (int, float)) else 0.0
            item_mem = NumericItem(mem_mb, f"{mem_mb:.1f}")
            item_mem.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(r, 0, item_pid)
            self.table.setItem(r, 1, item_name)
            self.table.setItem(r, 2, item_cpu)
            self.table.setItem(r, 3, item_mem)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table.verticalHeader().setDefaultSectionSize(24)

        self.table.setSortingEnabled(True)
        self.table.sortItems(sort_col, sort_order)

    def refresh_all(self):
        self._tick()

    def update_interval(self):
        ms = max(100, int(self.ui.SpinIntervalo.value()))
        self.timer.setInterval(ms)

    def kill_selected_process(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.information(self, "Kill", "Selecciona una fila primero.")
            return
        pid_item = self.table.item(row, 0)
        if not isinstance(pid_item, QTableWidgetItem) or not pid_item.text().isdigit():
            QMessageBox.warning(self, "Kill", "Selecciona una fila válida con PID.")
            return
        pid = int(pid_item.text())

        reply = QMessageBox.question(
            self, "Confirmar",
            f"¿Terminar proceso PID {pid}?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply != QMessageBox.Yes:
            return

        try:
            p = psutil.Process(pid)
            p.terminate()
            _, alive = psutil.wait_procs([p], timeout=2)
            if alive:
                p.kill()
            QMessageBox.information(self, "Kill", f"Proceso {pid} terminado.")
        except psutil.NoSuchProcess:
            QMessageBox.warning(self, "Kill", "El proceso ya no existe.")
        except psutil.AccessDenied:
            QMessageBox.critical(self, "Kill", "Permiso denegado. Ejecuta como admin si es necesario.")
        except Exception as e:
            QMessageBox.critical(self, "Kill", f"Error: {e}")
        finally:
            self.refresh_table()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
