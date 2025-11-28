"""
H1Z1 Just Survive Anti-AFK Script
Simulates periodic input to prevent AFK kick
"""

import pyautogui
import time
import random
import keyboard

# Configuration
CHECK_INTERVAL = 120  # Check every 2 minutes (120 seconds)
MOVEMENT_KEYS = ['w', 'a', 's', 'd']  # Basic movement keys
ENABLE_MOUSE_MOVEMENT = True
ENABLE_KEY_PRESSES = True

# Safety settings
pyautogui.FAILSAFE = True  # Move mouse to corner to stop script
pyautogui.PAUSE = 0.1  # Small pause between actions

print("=" * 50)
print("H1Z1 Just Survive Anti-AFK Script")
print("=" * 50)
print("\nSafety: Move mouse to top-left corner to emergency stop")
print("Press 'ESC' key to stop the script gracefully")
print(f"\nScript will perform actions every {CHECK_INTERVAL} seconds")
print("\nStarting in 5 seconds...")
print("Make sure H1Z1 is the active window!")
time.sleep(5)

def perform_movement():
    """Simulate a brief movement action"""
    if ENABLE_KEY_PRESSES:
        # Choose a random movement key
        key = random.choice(MOVEMENT_KEYS)
        print(f"Pressing '{key}' key...")
        
        # Press and hold briefly
        pyautogui.keyDown(key)
        time.sleep(random.uniform(0.1, 0.3))
        pyautogui.keyUp(key)

def perform_mouse_movement():
    """Simulate small mouse movements"""
    if ENABLE_MOUSE_MOVEMENT:
        # Get current mouse position
        current_x, current_y = pyautogui.position()
        
        # Small random movement (simulates looking around slightly)
        offset_x = random.randint(-50, 50)
        offset_y = random.randint(-30, 30)
        
        new_x = current_x + offset_x
        new_y = current_y + offset_y
        
        print(f"Moving mouse slightly...")
        pyautogui.moveTo(new_x, new_y, duration=random.uniform(0.2, 0.5))

def perform_jump():
    """Occasionally perform a jump action"""
    if random.random() < 0.3:  # 30% chance to jump
        print("Performing jump...")
        pyautogui.press('space')

try:
    action_count = 0
    print("\n[ACTIVE] Script is now running...\n")
    
    while True:
        # Check if ESC key is pressed
        if keyboard.is_pressed('esc'):
            print("\n[STOPPED] ESC key detected. Exiting...")
            break
        
        action_count += 1
        print(f"\n--- Action #{action_count} at {time.strftime('%H:%M:%S')} ---")
        
        # Perform random actions
        perform_movement()
        time.sleep(random.uniform(0.3, 0.7))
        
        perform_mouse_movement()
        time.sleep(random.uniform(0.2, 0.5))
        
        perform_jump()
        
        print(f"Waiting {CHECK_INTERVAL} seconds until next action...")
        
        # Sleep with periodic ESC checks
        for _ in range(CHECK_INTERVAL):
            if keyboard.is_pressed('esc'):
                print("\n[STOPPED] ESC key detected. Exiting...")
                raise KeyboardInterrupt
            time.sleep(1)

except KeyboardInterrupt:
    print("\n[STOPPED] Script terminated by user")
except pyautogui.FailSafeException:
    print("\n[STOPPED] Failsafe triggered (mouse moved to corner)")
except Exception as e:
    print(f"\n[ERROR] An error occurred: {e}")
finally:
    print("\nScript has ended. You can close this window.")

