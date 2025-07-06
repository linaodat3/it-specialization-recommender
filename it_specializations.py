# IT Specialization Recommender - Console Version
# Author: Lina (with ChatGPT guidance)
# Purpose: Help new university students choose their IT major based on interests and personality

import json

# -----------------------------
# Data Section
# -----------------------------

specializations = {
    "Computer Science": {
        "desc": "Focuses on problem-solving, programming, algorithms, and the theory behind computing.",
        "personality_fit": ["logical", "curious", "independent"],
        "expert": "Dr. Omar Alsharif",
        "email": "omar.cs@university.edu"
    },
    "Information Systems": {
        "desc": "Blends IT with business. Great for those who like organizing, analyzing, and improving processes.",
        "personality_fit": ["organized", "business-minded", "communicative"],
        "expert": "Eng. Hala Ibrahim",
        "email": "hala.is@university.edu"
    },
    "Networks": {
        "desc": "Covers infrastructure, data transfer, security, and managing communication systems.",
        "personality_fit": ["technical", "hands-on", "detail-oriented"],
        "expert": "Mr. Khaled Naser",
        "email": "khaled.networks@university.edu"
    },
    "Cybersecurity": {
        "desc": "Focuses on protecting systems, detecting threats, and ethical hacking.",
        "personality_fit": ["observant", "strategic", "cautious"],
        "expert": "Dr. Sara Ayoub",
        "email": "sara.cyber@university.edu"
    },
    "Software Engineering": {
        "desc": "Emphasizes structured software development, team projects, and real-world application design.",
        "personality_fit": ["team-player", "planner", "creative"],
        "expert": "Eng. Nidal Rahman",
        "email": "nidal.se@university.edu"
    },
    "Artificial Intelligence": {
        "desc": "Teaches machines to learn, decide, and solve problems intelligently.",
        "personality_fit": ["innovative", "curious", "analytical"],
        "expert": "Dr. Reem Haddad",
        "email": "reem.ai@university.edu"
    }
}

# -----------------------------
# Personality Quiz Section
# -----------------------------

def ask_questions():
    print("\n🧠 Answer the following to discover your ideal IT specialization:")
    answers = []

    questions = [
        ("Do you enjoy solving logic puzzles or coding challenges?", "logical"),
        ("Do you like coming up with new ideas or creative solutions?", "creative"),
        ("Are you interested in how machines think and learn?", "innovative"),
        ("Do you enjoy organizing data, planning, and making decisions?", "planner"),
        ("Do you like analyzing business workflows or improving systems?", "business-minded"),
        ("Are you detail-oriented and good at spotting patterns or issues?", "observant"),
        ("Would you prefer hands-on setup of systems like routers or servers?", "hands-on"),
        ("Are you someone who likes working in a team and sharing ideas?", "team-player"),
        ("Do you get excited by detecting security flaws or system breaches?", "strategic"),
        ("Are you good at explaining things to people or bridging tech and non-tech?", "communicative")
    ]

    for q, trait in questions:
        ans = input(f"\n{q} (yes/no): ").strip().lower()
        if ans == "yes":
            answers.append(trait)

    return answers

# -----------------------------
# Matching Algorithm
# -----------------------------

def recommend_specialization(traits):
    print("\n🔍 Analyzing your answers...\n")
    scores = {}
    for spec, data in specializations.items():
        score = sum(trait in traits for trait in data["personality_fit"])
        scores[spec] = score

    sorted_specs = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    top_spec = sorted_specs[0][0]
    top_info = specializations[top_spec]

    print(f"🎓 Based on your personality, your recommended specialization is: \033[1m{top_spec}\033[0m")
    print(f"\n📝 Description: {top_info['desc']}")
    print(f"👤 Expert: {top_info['expert']} (📧 {top_info['email']})\n")

    print("💬 Want to explore more? Here are other strong matches:")
    for spec, score in sorted_specs[1:3]:
        print(f"- {spec}: {score} matching traits")

# -----------------------------
# Expert Opinion Section
# -----------------------------

def show_expert_opinions():
    print("\n👩‍🏫 Expert Opinions:")
    for spec, data in specializations.items():
        print(f"\n🔸 {spec}\n{data['desc']}\nContact: {data['expert']} – {data['email']}")

# -----------------------------
# Main Program
# -----------------------------

def main():
    print("==============================")
    print("🎓 IT Specialization Recommender")
    print("==============================")

    while True:
        print("\nMenu:")
        print("1. Take the Personality Quiz")
        print("2. View Expert Opinions")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            traits = ask_questions()
            recommend_specialization(traits)
        elif choice == "2":
            show_expert_opinions()
        elif choice == "3":
            print("\n👋 Thank you for using the Recommender. Best of luck in your IT journey!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
