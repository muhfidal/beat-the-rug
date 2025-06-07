import pyautogui
import time
import random
import numpy as np
from colorama import init, Fore, Style
import sys
import os

init(autoreset=True)

def is_valid_button_size(btn, min_width=30, max_width=200, min_height=20, max_height=100):
    return (min_width <= btn.width <= max_width and 
            min_height <= btn.height <= max_height)

def is_green_button(region_img):
    arr = np.array(region_img)
    green_mean = arr[...,1].mean()
    red_mean = arr[...,0].mean()
    blue_mean = arr[...,2].mean()
    return green_mean > 45 and green_mean > red_mean + 5 and green_mean > blue_mean + 5

def is_active_play_button(region_img):
    arr = np.array(region_img)
    green_mean = arr[...,1].mean()
    red_mean = arr[...,0].mean()
    blue_mean = arr[...,2].mean()
    # Threshold hasil analisis data
    return green_mean > 45 and blue_mean > 48 and red_mean < 30

def is_active_spin_button(region_img):
    arr = np.array(region_img)
    green_mean = arr[...,1].mean()
    red_mean = arr[...,0].mean()
    blue_mean = arr[...,2].mean()
    return (
        green_mean > 80 and red_mean > 80 and blue_mean > 80 and
        abs(green_mean - red_mean) < 3 and
        abs(green_mean - blue_mean) < 3 and
        abs(red_mean - blue_mean) < 3
    )

# Clear screen otomatis
os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.CYAN + Style.BRIGHT + "==============================")
print(Fore.CYAN + Style.BRIGHT + "=== AUTO MINING FREE SPIN CUAN MEXX ===")
print(Fore.CYAN + Style.BRIGHT + "==============================")
print(Fore.MAGENTA + Style.BRIGHT + "SCRIPT INI BUATAN KTUPAT, GABOLE DISEBAR PUKI!")
print(Fore.WHITE + "PASTIKAN SEMUA FILE GAMBAR TOMBOL ADA DI FOLDER YANG SAMA DENGAN SCRIPT INI.")
print(Fore.YELLOW + "\n==============================")
print(Fore.YELLOW + "PILIH MENU:")
print(Fore.YELLOW + "1. MINING FREE SPIN")
print(Fore.YELLOW + "2. SPIN OTOMATIS")
print(Fore.YELLOW + "3. AUTO RUG KIMAK!")
print(Fore.YELLOW + "4. EXIT")
print(Fore.YELLOW + "==============================")
user_input = input(Fore.GREEN + "INPUT : ")
if user_input.strip() == "1":
    print(Fore.YELLOW + "\nTUNGGU 5 DETIK UNTUK SIAPKAN LAYAR...")
    time.sleep(5)
elif user_input.strip() == "2":
    print(Fore.CYAN + "\nMODE SPIN OTOMATIS AKTIF! (CTRL+C UNTUK KELUAR)")
    time.sleep(2)
    try:
        while True:
            # 1. Deteksi dan klik tombol menu SPIN (prioritas utama)
            try:
                menu_spin_buttons = list(pyautogui.locateAllOnScreen('img/menu_spin_button.png', confidence=0.85))
            except Exception:
                menu_spin_buttons = []
            if menu_spin_buttons:
                btn = max(menu_spin_buttons, key=lambda b: pyautogui.center(b).y)
                center = pyautogui.center(btn)
                print(Fore.CYAN + "MASUK MENU SPIN, SIAP-SIAP CUAN!")
                pyautogui.moveTo(center.x, center.y, duration=0.2)
                pyautogui.click()
                time.sleep(0.1)
                continue
            # 2. Deteksi dan klik tombol OK (day & night)
            try:
                ok_buttons_day = list(pyautogui.locateAllOnScreen('img/ok_button_day.png', confidence=0.80))
            except Exception:
                ok_buttons_day = []
            try:
                ok_buttons_night = list(pyautogui.locateAllOnScreen('img/ok_button_night.png', confidence=0.80))
            except Exception:
                ok_buttons_night = []
            ok_buttons = ok_buttons_day + ok_buttons_night
            if ok_buttons:
                for btn in ok_buttons:
                    center = pyautogui.center(btn)
                    print(Fore.YELLOW + "SIAP BOSQUE, OK DULU BIAR LANCAR!")
                    pyautogui.moveTo(center.x, center.y, duration=0.2)
                    pyautogui.click()
                    time.sleep(0.1)
                continue
            # 3. Deteksi dan klik tombol CLOSE
            try:
                close_buttons = list(pyautogui.locateAllOnScreen('img/close_button.png', confidence=0.85))
            except Exception:
                close_buttons = []
            if close_buttons:
                btn = max(close_buttons, key=lambda b: pyautogui.center(b).y)
                center = pyautogui.center(btn)
                print(Fore.RED + "TUTUPIN AJA, BIAR GAK KETAHUAN!")
                pyautogui.moveTo(center.x, center.y, duration=0.2)
                pyautogui.click()
                time.sleep(0.1)
                continue
            # 4. Deteksi dan klik tombol BEAT THE RUG
            try:
                beat_buttons = list(pyautogui.locateAllOnScreen('img/beat_the_rug_button.png', confidence=0.85))
            except Exception:
                beat_buttons = []
            if beat_buttons:
                btn = max(beat_buttons, key=lambda b: pyautogui.center(b).y)
                center = pyautogui.center(btn)
                print(Fore.WHITE + "HANTAM KARPETNYA BOS!")
                pyautogui.moveTo(center.x, center.y, duration=0.2)
                pyautogui.click()
                time.sleep(0.01)
                continue
            # 5. Deteksi dan klik tombol SPIN
            try:
                spin_buttons = list(pyautogui.locateAllOnScreen('img/spin_button.png', confidence=0.85))
            except Exception:
                spin_buttons = []
            if spin_buttons:
                for i, btn in enumerate(spin_buttons):
                    region = (int(btn.left), int(btn.top), int(btn.width), int(btn.height))
                    button_region = pyautogui.screenshot(region=region)
                    if is_active_spin_button(button_region):
                        center = pyautogui.center(btn)
                        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "JP BOSS!")
                        pyautogui.moveTo(center.x, center.y, duration=0.2)
                        pyautogui.click()
                        time.sleep(0.1)
                continue
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nSPIN OTOMATIS DIHENTIKAN. BALIK KE MENU UTAMA!")
        sys.exit(0)
elif user_input.strip() == "3":
    print(Fore.CYAN + "FITUR AUTO RUG KIMAK MASIH COMING SOON, TUNGGU UPDATE DARI KTUPAT!")
    sys.exit(0)
elif user_input.strip() == "4":
    print(Fore.WHITE + "KELUAR DARI SCRIPT. SAMPAI JUMPA DAN SEMOGA CUAN DI LAIN WAKTU!")
    sys.exit(0)
else:
    print(Fore.RED + "PILIHAN TIDAK VALID. KELUAR DARI SCRIPT.")
    sys.exit(0)

while True:
    # 1. Deteksi dan klik tombol OK (prioritas utama, dua versi gambar, confidence lebih tinggi)
    try:
        ok_buttons_day = list(pyautogui.locateAllOnScreen('img/ok_button_day.png', confidence=0.80))
        ok_buttons_day = [btn for btn in ok_buttons_day if is_valid_button_size(btn)]
    except Exception:
        ok_buttons_day = []

    try:
        ok_buttons_night = list(pyautogui.locateAllOnScreen('img/ok_button_night.png', confidence=0.80))
        ok_buttons_night = [btn for btn in ok_buttons_night if is_valid_button_size(btn)]
    except Exception:
        ok_buttons_night = []

    ok_buttons = ok_buttons_day + ok_buttons_night

    if ok_buttons:
        for btn in ok_buttons:
            center = pyautogui.center(btn)
            print(Fore.YELLOW + "SIAP BOSQUE, OK DULU BIAR LANCAR!")
            pyautogui.moveTo(center.x, center.y, duration=0.2)
            pyautogui.click()
            time.sleep(0.1)
        continue

    # 2. Deteksi dan klik tombol WATCH (prioritas kedua, benar-benar utama setelah OK)
    try:
        watch_buttons = list(pyautogui.locateAllOnScreen('img/watch_button.png', confidence=0.85))
    except Exception:
        watch_buttons = []

    if watch_buttons:
        btn = max(watch_buttons, key=lambda b: pyautogui.center(b).y)
        center = pyautogui.center(btn)
        print(Fore.MAGENTA + "NONTON DULU, SIAPA TAU DAPET CUAN!")
        pyautogui.moveTo(center.x, center.y, duration=0.2)
        pyautogui.click()
        time.sleep(0.1)
        continue

    # 3. Deteksi dan klik tombol CLOSE (prioritas ketiga)
    try:
        close_buttons = list(pyautogui.locateAllOnScreen('img/close_button.png', confidence=0.85))
    except Exception:
        close_buttons = []

    if close_buttons:
        btn = max(close_buttons, key=lambda b: pyautogui.center(b).y)
        center = pyautogui.center(btn)
        print(Fore.RED + "TUTUPIN AJA, BIAR GAK KETAHUAN!")
        pyautogui.moveTo(center.x, center.y, duration=0.2)
        pyautogui.click()
        time.sleep(0.1)
        continue

    # 4. Deteksi dan klik tombol CLAIM jika ada
    try:
        claim_buttons = list(pyautogui.locateAllOnScreen('img/claim_button.png', confidence=0.7))
    except Exception:
        claim_buttons = []

    if claim_buttons:
        btn = max(claim_buttons, key=lambda b: pyautogui.center(b).y)
        center = pyautogui.center(btn)
        print(Fore.CYAN + "CLAIM DULU, REJEKI GAK BOLEH LEWAT!")
        pyautogui.moveTo(center.x, center.y, duration=0.2)
        pyautogui.click()
        time.sleep(0.1)
        continue

    # 5. Deteksi dan klik tombol BEAT THE RUG jika ada
    try:
        beat_buttons = list(pyautogui.locateAllOnScreen('img/beat_the_rug_button.png', confidence=0.85))
    except Exception:
        beat_buttons = []

    if beat_buttons:
        btn = max(beat_buttons, key=lambda b: pyautogui.center(b).y)
        center = pyautogui.center(btn)
        print(Fore.WHITE + "HANTAM KARPETNYA BOS!")
        pyautogui.moveTo(center.x, center.y, duration=0.2)
        pyautogui.click()
        time.sleep(0.01)
        continue

    # 6. Deteksi dan klik tombol PLAY
    try:
        play_buttons = list(pyautogui.locateAllOnScreen('img/play_button.png', confidence=0.85))
        play_buttons = [btn for btn in play_buttons if is_valid_button_size(btn)]
        active_play_buttons = []
        for btn in play_buttons:
            try:
                region = (int(btn.left), int(btn.top), int(btn.width), int(btn.height))
                button_region = pyautogui.screenshot(region=region)
                if is_active_play_button(button_region):
                    active_play_buttons.append(btn)
            except Exception as e:
                pass
        play_buttons = active_play_buttons
    except Exception:
        play_buttons = []

    if play_buttons:
        btn = max(play_buttons, key=lambda b: pyautogui.center(b).y)
        center = pyautogui.center(btn)
        print(Fore.BLUE + "GAS MAIN LAGI, JANGAN KENDOR!")
        pyautogui.moveTo(center.x, center.y, duration=0.2)
        pyautogui.click()
        time.sleep(0.1)
        continue

    # 8. Deteksi dan klik tombol SPIN jika ada
    try:
        spin_buttons = list(pyautogui.locateAllOnScreen('img/spin_button.png', confidence=0.85))
    except Exception:
        spin_buttons = []

    if spin_buttons:
        for i, btn in enumerate(spin_buttons):
            region = (int(btn.left), int(btn.top), int(btn.width), int(btn.height))
            button_region = pyautogui.screenshot(region=region)
            arr = np.array(button_region)
            green_mean = arr[...,1].mean()
            red_mean = arr[...,0].mean()
            blue_mean = arr[...,2].mean()
            if is_active_spin_button(button_region):
                center = pyautogui.center(btn)
                print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "MUTERIN RODA CUAN!")
                pyautogui.moveTo(center.x, center.y, duration=0.2)
                pyautogui.click()
                time.sleep(0.1)
        continue

    # 9. Deteksi dan klik tombol SELL jika ada
    try:
        sell_buttons = list(pyautogui.locateAllOnScreen('img/sell_button.png', confidence=0.90))
        sell_buttons = [btn for btn in sell_buttons if is_valid_button_size(btn)]
        active_sell_buttons = []
        for btn in sell_buttons:
            try:
                region = (int(btn.left), int(btn.top), int(btn.width), int(btn.height))
                button_region = pyautogui.screenshot(region=region)
                if is_green_button(button_region):
                    active_sell_buttons.append(btn)
            except Exception as e:
                pass
        sell_buttons = active_sell_buttons
    except Exception as e:
        sell_buttons = []

    if sell_buttons:
        btn = max(sell_buttons, key=lambda b: pyautogui.center(b).y)
        center = pyautogui.center(btn)
        print(Fore.GREEN + "JUAL SEKARANG, JANGAN SAMPE RUGI!")
        pyautogui.moveTo(center.x, center.y, duration=0.2)
        pyautogui.click()
        time.sleep(2.5)
        continue

    time.sleep(0.1)