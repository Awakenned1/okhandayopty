from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/services')
def services():
    return render_template('services.html')




@app.route('/projects')
def projects():
    # Project data
    projects = [
        {
            'title': 'Urban Development',
            'description': 'This project focuses on the redevelopment of urban areas, enhancing infrastructure, and providing modern residential solutions.',
            'image': 'highway.jpg'
        },
        {
            'title': 'Green Parks Initiative',
            'description': 'Our initiative aims to create green recreational parks that offer sustainable environments and community gathering spaces.',
            'image': 'pipline.jpg'
        },
        {
            'title': 'Highway Expansion',
            'description': 'This project includes the expansion of highways to improve traffic flow and reduce congestion in highly populated areas.',
            'image': 'truck.jpg'
        },
        {
            'title': 'Building Project',
            'description': 'Our project focuses on sustainable and innovative building techniques to meet modern urban demands.',
            'image': 'building.jpg'
        },
        {
            'title': 'Logistics Improvement',
            'description': 'Improving logistics infrastructure to ensure efficient and reliable transportation of goods.',
            'image': 'trucker.jpg'
        },
        {
            'title': 'Infrastructure Development',
            'description': 'Developing essential infrastructure to support community growth and economic development.',
            'image': 'work.jpg'
        },
        {
            'title': 'Public Spaces Enhancement',
            'description': 'Creating and enhancing public spaces to promote social interaction and community engagement.',
            'image': 'sider.jpg'
        },
        {
            'title': 'Sidewalk Improvement',
            'description': 'Improving sidewalks to ensure pedestrian safety and accessibility in urban areas.',
            'image': 'sideworkroad.jpg'
        },
        {
            'title': 'Road Maintenance',
            'description': 'Maintaining and repairing roads to ensure safe and efficient transportation.',
            'image': 'POTHOLES.jpg'
        }
    ]

    return render_template('projects.html', projects=projects)


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
