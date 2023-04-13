from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static")

user = {
    "name": "Adam Nagy",
    "introduction": "Software engineer focused on full stack development with over 20 years of programming experience.",
    "email": "devdracon@gmail.com",
    "skills": [
        "ReactJS",
        "Redux",
        "Typescript",
        "Node.js",
        "Express",
        "javascript",
        "Python",
        "Django",
        "Flask",
        "Cypress",
        "Selenium",
        "MongoDB",
        "SQL",
        "HTML",
        "CSS",
        "SASS",
        "styled components",
        "git",
        "docker",
    ],
    "projects": {
        0: {
            "name": "Screen Saga: Find movies and recommendations",
            "github_link": "https://github.com/DraconDev/screensaga",
            "description": "Next SWR Typescript MUI Vercel OMDB_API YOUTUBE_API",
            "host_link": "https://screensaga-k8ou.vercel.app/",
            "image_path": "images/thumbs/screen_saga.jpg",
        },
        1: {
            "name": "Amazon Store",
            "github_link": "https://github.com/Nadaga/amazon-clone",
            "description": "React Redux Typescript SCSS Firebase",
            "host_link": "https://heuristic-wing-b57de6.netlify.app/",
            "image_path": "images/thumbs/amazonStore.jpg",
        },
        2: {
            "name": "Movie Site",
            "github_link": "https://github.com/Nadaga/movie-site",
            "description": "React Javascript MUI Firebase",
            "host_link": "https://movie-site-f90c7.web.app/",
            "image_path": "images/thumbs/movieSite.jpg",
        },
        3: {
            "name": "This portfolio",
            "github_link": "https://github.com/DraconDev/portfolio_flask",
            "description": "Python Flask Jinja Javascript HTML SASS CSS",
            "host_link": "/",
            "image_path": "images/thumbs/portfolio.jpg",
        },
    },
}


@app.route("/")
def index():
    return render_template("index.html", **user)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
