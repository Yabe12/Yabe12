import requests
import re

# GitHub username
username = 'Yabe12'

# URLs to fetch data
contributions_url = f'https://github-readme-stats.vercel.app/api?username={username}&count_private=true'
streak_url = f'https://github-readme-streak-stats.herokuapp.com/?user={username}&theme=dark'

# Fetch contribution stats
contributions_data = requests.get(contributions_url).text
streak_data = requests.get(streak_url).text

# Extract the contributions count
contributions = re.search(r'"totalContributions":(\d+)', contributions_data).group(1)
longest_streak = re.search(r'"longestStreak":(\d+)', streak_data).group(1)

# Read the README.md
with open('README.md', 'r') as file:
    readme = file.read()

# Replace the contributions and streak placeholders
readme = re.sub(r'Contributions:\s*\d+', f'Contributions: {contributions}', readme)
readme = re.sub(r'Longest Streak:\s*\d+', f'Longest Streak: {longest_streak}', readme)

# Write the updated README.md
with open('README.md', 'w') as file:
    file.write(readme)
