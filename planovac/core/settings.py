import datetime

class Settings:
    bank_holidays = []

    @staticmethod
    def get_bank_holidays():
        if len(Settings.bank_holidays) == 0:
            Settings._load_holidays()
        return Settings.bank_holidays

    @staticmethod
    def _load_holidays():
        pass

    
