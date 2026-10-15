"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Club": {
        "description": "Practice basketball skills and play friendly games",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Track and Field": {
        "description": "Train for running, jumping, and throwing events",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 25,
        "participants": []
    },
    "Art Club": {
        "description": "Explore drawing, painting, and other visual arts",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": []
    },
    "Drama Club": {
        "description": "Develop acting skills and create theatrical performances",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Debate Club": {
        "description": "Research topics and practice persuasive public speaking",
        "schedule": "Mondays, 3:30 PM - 4:30 PM",
        "max_participants": 15,
        "participants": []
    },
    "Science Club": {
        "description": "Explore scientific ideas through experiments and projects",
        "schedule": "Fridays, 3:30 PM - 4:30 PM",
        "max_participants": 18,
        "participants": []
    },
    "Soccer Club": {
        "description": "Practice soccer skills and play team matches",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 22,
        "participants": []
    },
    "Volleyball Club": {
        "description": "Learn volleyball techniques and play friendly games",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": []
    },
    "Photography Club": {
        "description": "Learn photography techniques and create visual stories",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": []
    },
    "Music Club": {
        "description": "Explore music through listening, practice, and performances",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Math Club": {
        "description": "Solve challenging problems and explore mathematical ideas",
        "schedule": "Mondays, 3:30 PM - 4:30 PM",
        "max_participants": 16,
        "participants": []
    },
    "Creative Writing Club": {
        "description": "Develop writing skills and share original stories and poems",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 16,
        "participants": []
    },
    "Tennis Club": {
        "description": "Practice tennis skills and play friendly matches",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": []
    },
    "Swimming Club": {
        "description": "Improve swimming technique and build water confidence",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Ceramics Club": {
        "description": "Learn hand-building and pottery techniques",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": []
    },
    "Film Club": {
        "description": "Explore filmmaking and discuss visual storytelling",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": []
    },
    "Robotics Club": {
        "description": "Design, build, and program robots to solve challenges",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": []
    },
    "History Club": {
        "description": "Investigate historical events, people, and civilizations",
        "schedule": "Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 16,
        "participants": []
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

   # Validate student is not already signed up
   if email in activity["participants"]:
     raise HTTPException(status_code=400, detail="Student is already signed up")

   # Add student
   activity["participants"].append(email)
   return {"message": f"Signed up {email} for {activity_name}"}