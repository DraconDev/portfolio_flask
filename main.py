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
        "CSSS",
        "SASS",
        "styled components",
        "git",
        "docker",
    ],
    "projects": {
        0: {
            "name": "Amazon Store",
            "github_link": "https://github.com/Nadaga/amazon-clone",
            "description": "React Redux Typescript SCSS Firebase",
            "host_link": "https://heuristic-wing-b57de6.netlify.app/",
            "image_path": "images/thumbs/amazonStore.jpg",
        },
        1: {
            "name": "Movie Site",
            "github_link": "https://github.com/Nadaga/movie-site",
            "description": "React Javascript REST MUI Firebase",
            "host_link": "https://movie-site-f90c7.web.app/",
            "image_path": "images/thumbs/movieSite.jpg",
        },
        2: {
            "name": "This portfolio",
            "github_link": "https://github.com/Nadaga/movie-site",
            "description": "Python Flask Jinja Javascript HTML SASS CSS",
            "host_link": "https://movie-site-f90c7.web.app/",
            "image_path": "images/thumbs/portfolio.jpg",
        },
    },
}


@app.route("/")
def index():
    return render_template("index.html", **user)


if __name__ == "__main__":
    app.run(debug=True)
