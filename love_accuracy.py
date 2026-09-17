import random

print("=" * 40)
print("       💕 LOVE ACCURACY TEST 💕")
print("=" * 40)

your_name = input("Enter your name: ")
gf_name = input("Enter your GF's name: ")

print("\nCalculating your love accuracy... ❤️")

love_accuracy = random.randint(85, 100)

print("\n" + "=" * 40)
print(f"💖 {your_name} ❤️ {gf_name}")
print(f"Love Accuracy: {love_accuracy}%")
print("=" * 40)

if love_accuracy >= 95:
    print("💍 Perfect Couple! Made for each other!")
elif love_accuracy >= 90:
    print("🥰 True Love! You both are special!")
else:
    print("❤️ Love is growing stronger every day!")

print("\nThis love is forever! 💕")
