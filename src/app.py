"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI(title="Mergington High School Activities API",
              description="API for viewing and signing up for extracurricular activities")

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
    }
}

# In-memory student database
students = {
    "michael@mergington.edu": {"name": "Michael Smith", "grade": 10},
    "daniel@mergington.edu": {"name": "Daniel Johnson", "grade": 11},
    "emma@mergington.edu": {"name": "Emma Davis", "grade": 9},
    "sophia@mergington.edu": {"name": "Sophia Wilson", "grade": 12},
    "john@mergington.edu": {"name": "John Brown", "grade": 10},
    "olivia@mergington.edu": {"name": "Olivia Miller", "grade": 11}
}


@app.get("/")
def root():
    """Welcome message with API information"""
    return {
        "message": "Welcome to Mergington High School Activities API", 
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/activities")
def get_activities():
    """Get all activities with their details and current participant count"""
    enhanced_activities = {}
    for name, activity in activities.items():
        enhanced_activities[name] = {
            "description": activity["description"],
            "schedule": activity["schedule"],
            "max_participants": activity["max_participants"],
            "participants": activity["participants"],
            "current_participant_count": len(activity["participants"])
        }
    return enhanced_activities


@app.get("/students")
def get_students():
    """Get all registered students"""
    return students


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]
    
    # Check if already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Already signed up for this activity")
    
    # Check if activity is full
    if len(activity["participants"]) >= activity["max_participants"]:
        raise HTTPException(status_code=400, detail="Activity is full")

    # Add student to activity
    activity["participants"].append(email)
    
    # If student doesn't exist in our database, add them with default info
    if email not in students:
        # Extract name from email (simple approach)
        name = email.split("@")[0].replace(".", " ").title()
        students[email] = {"name": name, "grade": 9}  # Default grade
    
    return {
        "message": f"Successfully signed up {email} for {activity_name}",
        "activity": activity_name,
        "student_email": email,
        "current_participants": len(activity["participants"])
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)# filepath: /Users/a266392/git_exercise/skills-getting-started-with-github-copilot/src/app.py
"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI(title="Mergington High School Activities API",
              description="API for viewing and signing up for extracurricular activities")

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
    }
}

# In-memory student database
students = {
    "michael@mergington.edu": {"name": "Michael Smith", "grade": 10},
    "daniel@mergington.edu": {"name": "Daniel Johnson", "grade": 11},
    "emma@mergington.edu": {"name": "Emma Davis", "grade": 9},
    "sophia@mergington.edu": {"name": "Sophia Wilson", "grade": 12},
    "john@mergington.edu": {"name": "John Brown", "grade": 10},
    "olivia@mergington.edu": {"name": "Olivia Miller", "grade": 11}
}


@app.get("/")
def root():
    """Welcome message with API information"""
    return {
        "message": "Welcome to Mergington High School Activities API", 
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/activities")
def get_activities():
    """Get all activities with their details and current participant count"""
    enhanced_activities = {}
    for name, activity in activities.items():
        enhanced_activities[name] = {
            "description": activity["description"],
            "schedule": activity["schedule"],
            "max_participants": activity["max_participants"],
            "participants": activity["participants"],
            "current_participant_count": len(activity["participants"])
        }
    return enhanced_activities


@app.get("/students")
def get_students():
    """Get all registered students"""
    return students


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]
    
    # Check if already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Already signed up for this activity")
    
    # Check if activity is full
    if len(activity["participants"]) >= activity["max_participants"]:
        raise HTTPException(status_code=400, detail="Activity is full")

    # Add student to activity
    activity["participants"].append(email)
    
    # If student doesn't exist in our database, add them with default info
    if email not in students:
        # Extract name from email (simple approach)
        name = email.split("@")[0].replace(".", " ").title()
        students[email] = {"name": name, "grade": 9}  # Default grade
    
    return {
        "message": f"Successfully signed up {email} for {activity_name}",
        "activity": activity_name,
        "student_email": email,
        "current_participants": len(activity["participants"])
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)