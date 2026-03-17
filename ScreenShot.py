import pyscreenshot
import os
from datetime import datetime
import time

def take_screenshot(region=None, delay=0, filename=None):
    """
    Take a screenshot with options
    region: (x1,y1,x2,y2) for specific area
    delay: wait seconds before taking shot
    filename: custom filename
    """
    
    if delay > 0:
        print(f"Taking screenshot in {delay} seconds...")
        time.sleep(delay)
    
    try:
        # Take screenshot
        if region:
            image = pyscreenshot.grab(bbox=region)
            print(f"Capturing region: {region}")
        else:
            image = pyscreenshot.grab()
            print("Capturing full screen")
        
        # Generate filename if not provided
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
        
        # Save
        image.save(filename)
        
        # Show file info
        file_size = os.path.getsize(filename) / 1024  # KB
        print(f"✅ Saved: {filename}")
        print(f"📊 Size: {file_size:.1f} KB")
        print(f"📏 Dimensions: {image.size[0]}x{image.size[1]}")
        
        return filename
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def quick_menu():
    """Simple menu for screenshot options"""
    print("\n" + "="*40)
    print("📸 SCREENSHOT TOOL")
    print("="*40)
    print("1. Full screen (now)")
    print("2. Full screen (3 sec delay)")
    print("3. Select region (click and drag)")
    print("4. Take 5 screenshots (1 sec apart)")
    print("5. Custom settings")
    print("0. Exit")
    
    choice = input("\nChoose (0-5): ")
    
    if choice == "1":
        take_screenshot()
    elif choice == "2":
        take_screenshot(delay=3)
    elif choice == "3":
        print("\nClick and drag to select area")
        print("Enter coordinates manually (x1 y1 x2 y2): ")
        try:
            x1, y1, x2, y2 = map(int, input().split())
            take_screenshot(region=(x1, y1, x2, y2))
        except:
            print("Invalid coordinates")
    elif choice == "4":
        print("Taking 5 screenshots...")
        for i in range(5):
            filename = f"burst_{i+1}.png"
            take_screenshot(filename=filename)
            time.sleep(1)
    elif choice == "5":
        print("\nCustom settings:")
        delay = int(input("Delay seconds (0 for none): "))
        name = input("Filename (enter for timestamp): ") or None
        take_screenshot(delay=delay, filename=name)
    elif choice == "0":
        return False
    return True

# Run the tool
if __name__ == "__main__":
    while quick_menu():
        input("\nPress Enter to continue...")
    print("Goodbye!")