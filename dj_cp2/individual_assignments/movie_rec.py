#DJ, 1st, Movie Recommender
import csv

def clear_screen(): print("\033c", end = "")

def load_movies():
    movies = []
    try:
        with open("dj_cp2/individual_assignments/movies.csv", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    movies.append({
                        "title": row["Title"].strip(),
                        "director": [x.strip().lower() for x in row["Director"].split(",")],
                        "genre": [x.strip().lower() for x in row["Genre"].split("/")],
                        "rating": row["Rating"].strip(),
                        "length": int(row["Length (min)"]),
                        "actors": [x.strip().lower() for x in row["Notable Actors"].split(",")]
                    })
                except:
                    pass
    except:
        pass
    return movies

def show_list(movies):
    if len(movies) == 0:
        print("No movies found.")
        return
    for i in range(len(movies)):
        print(str(i+1) + ". " + movies[i]["title"])

def show_details(movie):
    print("Title:", movie["title"])
    print("Director:", ", ".join([x.title() for x in movie["director"]]))
    print("Genre:", ", ".join([x.title() for x in movie["genre"]]))
    print("Rating:", movie["rating"])
    print("Length:", movie["length"], "minutes")
    print("Actors:", ", ".join([x.title() for x in movie["actors"]]))

def pick_movie(movies):
    while True:
        choice = input("Enter number for details or press Enter to return: ").strip()
        if choice == "":
            return
        if not choice.isdigit():
            print("Invalid choice.")
            continue
        num = int(choice)
        if num < 1 or num > len(movies):
            print("Invalid choice.")
            continue
        show_details(movies[num-1])
        back = input("Press Enter to return: ")

def filter_movies(movies, genre, director, actor, length_filter):
    results = []
    for m in movies:
        ok = True
        if genre and genre not in m["genre"]:
            ok = False
        if director and director not in m["director"]:
            ok = False
        if actor and actor not in m["actors"]:
            ok = False
        if length_filter:
            mode, v1, v2 = length_filter
            if mode == "<" and not (m["length"] < v1):
                ok = False
            if mode == ">" and not (m["length"] > v1):
                ok = False
            if mode == "=" and not (m["length"] == v1):
                ok = False
            if mode == "range" and not (v1 <= m["length"] <= v2):
                ok = False
        if ok:
            results.append(m)
    return results

def get_length():
    mode = input("Length filter (<, >, =, range) or Enter to skip: ").strip()
    if mode == "":
        return None
    if mode not in ["<", ">", "=", "range"]:
        print("Invalid choice.")
        return None
    if mode == "range":
        a = input("Minimum length: ").strip()
        b = input("Maximum length: ").strip()
        if a.isdigit() and b.isdigit():
            return ("range", int(a), int(b))
        return None
    val = input("Length value: ").strip()
    if val.isdigit():
        return (mode, int(val), None)
    return None

def search(movies):
    while True:
        genre = input("Genre or Enter to skip: ").strip().lower()
        director = input("Director or Enter to skip: ").strip().lower()
        actor = input("Actor or Enter to skip: ").strip().lower()

        length_filter = None
        length_choice = input("Do you want to filter by length? (yes/no): ").strip().lower()
        if length_choice == "yes":
            while True:
                choice = input("Choose type: 1) Exact  2) Less than  3) Greater than  4) Range: ").strip()
                if choice not in ["1","2","3","4"]:
                    print("Invalid choice.")
                    continue
                if choice == "1":
                    val = input("Enter exact length in minutes: ").strip()
                    if val.isdigit():
                        length_filter = ("=", int(val), None)
                        break
                elif choice == "2":
                    val = input("Enter maximum length in minutes: ").strip()
                    if val.isdigit():
                        length_filter = ("<", int(val), None)
                        break
                elif choice == "3":
                    val = input("Enter minimum length in minutes: ").strip()
                    if val.isdigit():
                        length_filter = (">", int(val), None)
                        break
                elif choice == "4":
                    min_val = input("Enter minimum length: ").strip()
                    max_val = input("Enter maximum length: ").strip()
                    if min_val.isdigit() and max_val.isdigit():
                        length_filter = ("range", int(min_val), int(max_val))
                        break
                print("Invalid numbers, please try again.")

        count = 0
        if genre: count += 1
        if director: count += 1
        if actor: count += 1
        if length_filter: count += 1

        if count < 2:
            print("Enter at least two search criteria.")
            continue

        results = filter_movies(movies, genre, director, actor, length_filter)
        print()
        show_list(results)
        pick_movie(results)
        return

def main():
    movies = load_movies()
    if len(movies) == 0:
        print("No movies loaded.")
        return

    while True:
        clear_screen()
        print("1. View full movie list")
        print("2. Search movies")
        print("3. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            show_list(movies)
            pick_movie(movies)
        elif choice == "2":
            search(movies)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

main()