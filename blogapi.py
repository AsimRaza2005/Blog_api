from flask import Flask, request, jsonify

app = Flask(__name__)

bloglist = [
    {
        "id": 1,
        "title": "How To Learn and Implement AI in Your Project",
        "description": "AI and data are the main part of any project; you implement them using many techniques."
    }
]

@app.route('/api/blogs', methods=['GET'])
def get_blogs():
    return jsonify(bloglist)

@app.route('/api/get_blog/<int:id>')

def get_blog(id):
    
    for blog in bloglist:
        
        if blog['id'] == id:
            
            return jsonify({"Data":bloglist}),200
        
    return jsonify({"message":"Blog not found"}),404 

@app.route('/api/add_blog',methods=['POST']) 

def add_blog():
    
    new_data = request.json
    new_data['id'] == bloglist
    
    bloglist.append(new_data)
    
    return jsonify({"message":"Data Added Successfully"}),201

@app.put('/api/update')
def update_blog():
    data = request.get_json()

    if not data or 'id' not in data or 'title' not in data or 'description' not in data:
        return jsonify({"message": "Invalid request. ID, title, and description are required"}), 400

    for item in bloglist:
        if item['id'] == data['id']:
            item['title'] = data['title']  # Fixed assignment
            item['description'] = data['description']  # Fixed assignment
            return jsonify({"message": "Data Updated Successfully"}), 200

    return jsonify({"message": "Blog not found"}), 404  # Improved response message

@app.route('/api/delete/<int:id>')

def delete_blog(id):
    
    for blog in bloglist:
        
        if blog['id'] == id:
            
            bloglist.remove(blog)
            
            return jsonify({"message":"Data Deleted Successfully"}),200
        
    return jsonify({"message":"Data Not Found"}),404


if __name__ == "__main__":
    app.run(debug=True)
