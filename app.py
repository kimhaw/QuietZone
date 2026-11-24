from flask import Flask, render_template_string, request

app = Flask(__name__)

STUDY_SPACES = [
    {
    "name": "MMU Library",
    "location": "Siti Hasmah Digital Library",
    "facilities": "Power sockets, Air-cond, Wi-Fi",
    "hours": "8:00 AM - 10:00 PM",
},
{  
    "name": "MMU Learning Point",
    "location": "Siti Hasmah Digital Library",
    "facilities": "Power sockets, Air-cond, Wi-Fi",
    "hours": "24/7",
},
{
  "name": "Zus Coffee MMU Cyberjaya",
  "location": "STAD / Student Centre, MMU Cyberjaya",
  "facilities": "Coffee counter & pickup; specific details on power sockets, air-conditioning, and Wi-Fi ",
  "hours": "7:00 AM - 9:40 PM (Mon-Sun)",
},
{
  "name": "FCI Student Lounge",
  "location": "Faculty of Computing & Informatics, MMU Cyberjaya",
  "facilities": "power sockets, air-conditioning, Wi-Fi; wheelchair-accessible entrance and parking noted for the faculty",
  "hours": "24/7"
},
{
  "name": "FOM Student Lounge",
  "location": "Faculty of Management, MMU Cyberjaya",
  "facilities": "power sockets, air-conditioning, Wi-Fi",
  "hours": "24/7"
},
{
  "name": "FCM Student Lounge (Space Bar)",
  "location": "Faculty of Creative Multimedia, MMU Cyberjaya",
  "facilities": "power sockets, air-conditioning, Wi-Fi",
  "hours": "24/7"
}
]

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>QuietZone - Study Space Directory</title>
</head>
<body>
    <h1>QuietZone - Study Space Directory</h1>
    <form method="GET">
        <input type="text" name="q" placeholder="Search by name or location..." value="{{ query }}">
        <button type="submit">Search</button>
    </form>
    <ul>
    {% for space in spaces %}
        <li>
            <p><strong>Name:</strong> {{ space.name }}</p>
            <p><strong>Location:</strong> {{ space.location }}</p>
            <p><strong>Facilities:</strong> {{ space.facilities }}</p>
            <p><strong>Hours:</strong> {{ space.hours }}</p>
        </li>
    {% else %}
        <li>No matching study spaces found.</li>
    {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/")
def directory():
    # Read what the user typed into the search box (default is empty string "")
    query = request.args.get("q", "").strip()

    if query:
        # Keep only spaces where the search text matches name or location (case-insensitive)
        filtered = [
            s for s in STUDY_SPACES
            if query.lower() in s["name"].lower() or query.lower() in s["location"].lower()
        ]
    else:
        filtered = STUDY_SPACES

    return render_template_string(HTML_PAGE, spaces=filtered, query=query)

if __name__ == "__main__":
    app.run(debug=True)