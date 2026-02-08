from stream_guidance import recommend_stream_class10
from career_guidance import recommend_career_class12

# -------- Class 10 Test --------
class10_marks = {
    "Maths": 59,
    "Science": 59,
    "Computer": 75,
    "Hindi": 55,
    "Social Science": 52
}

stream, reason = recommend_stream_class10(class10_marks)

print("\nClass 10 Stream Recommendation")
print("Recommended Stream:", stream)
print("Reason:", reason)


# -------- Class 12 Test --------
stream = "Non-Medical"
avg_500 = 320
activity_score = 4

career, colleges, advice = recommend_career_class12(stream, avg_500, activity_score)

print("\nClass 12 Career Recommendation")
print("Career Options:", career)
print("Colleges:", colleges)
print("Advice:", advice)