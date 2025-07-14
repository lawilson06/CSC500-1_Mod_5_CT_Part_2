"""
CSC500-1 Module 5 Critical Thinking Part 2 - Book Purchase Awards Program
Lawrence Wilson
July 13, 2025
"""

from BookClubAwards import BookClubAwards

csu_book_awards_obj = BookClubAwards()

points_awarded = csu_book_awards_obj.reward_return()

print(f"You have been awarded {points_awarded} points this month.")

