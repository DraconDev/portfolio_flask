from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static")

user = {
    "name": "Adam Nagy",
    "introduction": "Software engineer focused on full stack development with over 20 years of programming experience.",
    "email": "adamnagywork@gmail.com",
    # "skills": [
    #     "ReactJS",
    #     "Redux",
    #     "Typescript",
    #     "Node.js",
    #     "Express",
    #     "javascript",
    #     "Python",
    #     "Django",
    #     "Flask",
    #     "Cypress",
    #     "Selenium",
    #     "MongoDB",
    #     "SQL",
    #     "HTML",
    #     "CSS",
    #     "SASS",
    #     "styled components",
    #     "git",
    #     "docker",
    # ],
    "projects": {
        0: {
            "name": "Movie recommendations",
            "github_link": "https://github.com/DraconDev/screensaga",
            "description": "Next Typescript MUI SWR",
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
            "name": "Amazon Filter",
            "github_link": "https://github.com/DraconDev/Amazon-easyshop-filter-scraper",
            "description": "Next Typescript Tailwind Playwright Zustand",
            "host_link": "https://github.com/DraconDev/Amazon-easyshop-filter-scraper",
            "image_path": "images/thumbs/amazon_filter.jpg",
        },
        4: {
            "name": "This portfolio",
            "github_link": "https://github.com/DraconDev/portfolio_flask",
            "description": "Python Flask Jinja",
            "host_link": "/",
            "image_path": "images/thumbs/portfolio.jpg",
        },
    },
    "skills": {
        "Languages": [
            "Javascript",
            "Typescript",
            "Python",
            "Go",
            "Rust"
            "C++",
        ],
        "FrontEnd": [
            "React",
            "Next",
            "Redux",
            "Zustand",
            "Context",
        ],
        "BackEnd": ["Node", "Express", "Next", "Gin, ""Flask", "Django"],
        "Design": ["Tailwind","CSS", "SASS", "MUI", ],
        "Data & API": [
            "Mongo",
            "PostgreSQL",
            "AWS",
            "Firebase",
            "Supabase"
            "Redis",
        ],
        "Automation": ["Playwright", "Selenium"],
        # "Version Control": ["Git"],
    },
}



@app.route("/")
def index():
    return render_template("index.html", **user)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
