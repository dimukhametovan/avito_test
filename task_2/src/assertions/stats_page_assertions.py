class StatsAssertions:
    @staticmethod
    def timer_restarted(before: str, after: str):
        assert before != after, "Таймер не перезапустился после нажатия 'Обновить'"

    @staticmethod
    def progress_after_refresh(before: float, after: float):
        assert after <= before or after < 1.0, (
            f"Прогресс после обновления не выглядит сброшенным: было {before}, стало {after}"
        )

    @staticmethod
    def auto_update_is_running(is_running: bool):
        assert is_running, "Автообновление должно быть включено"

    @staticmethod
    def auto_update_is_running(is_running: bool):
        assert not is_running, "Автообновление должно быть выключено"

    @staticmethod
    def timer_stopped(before: str, after: str):
        assert before == after, "Таймер должен остановиться при выключении автообновления"

    @staticmethod
    def timer_resumed(before: str, after: str):
        assert before != after, "Таймер не возобновил отсчёт после включения автообновления"
