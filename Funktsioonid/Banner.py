def bannersize(slogan: str) -> str:
    return slogan.upper()

if __name__ == "__main__":
    repeat_count = int(input("Mitu korda soovite sloganit korrata?"))
    slogan = input("Sisetage enda slogan: ")
    banner_text = bannersize(slogan)
    print(f"{banner_text}\n" * repeat_count)