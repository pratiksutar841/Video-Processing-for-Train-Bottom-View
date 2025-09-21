<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

<h1>🚆 Train Coach Detection & Side View Coverage Report</h1>

<p>
A computer vision project to automate coach detection, splitting, and frame extraction from train side-view videos. The project is built as part of the <b>Machine Learning Internship Assignment</b> from <b>Soothsayer Analytics India Private Limited</b>.
</p>

<hr>

<h2>🔗 GitHub Repository</h2>
<p>
Visit the complete codebase on GitHub:<br>
<a href="https://github.com/pratiksutar841/Video-Processing-for-Train-Bottom-View.git" target="_blank">
https://github.com/pratiksutar841/Video-Processing-for-Train-Bottom-View.git
</a>
</p>

<hr>

<h2>📌 Project Objectives</h2>
<ul>
  <li>Split a full train video into separate videos for each coach.</li>
  <li>Count the number of wagons and engines.</li>
  <li>Extract minimum frames for full wagon coverage (nose to tail).</li>
  <li>Detect key components like open/closed doors.</li>
  <li>Generate structured image folders and an optional report.</li>
</ul>

<hr>

<h2>🛠️ Technologies Used</h2>
<ul>
  <li>Python, OpenCV, NumPy</li>
  <li>Video processing (frame splitting, object detection)</li>
  <li>Optional: YOLO / Contour Detection for feature identification</li>
</ul>

<hr>

<h2>📁 Project Structure</h2>
<pre>
project-folder/
│── main.py               # Main executable for processing
│── utils.py              # Helper functions
│── requirements.txt      # Python dependencies
│── sample_input/         # Raw input train videos
│── output/               # Processed coach videos and frames
│── README.in             # This HTML documentation
</pre>

<hr>

<h2>🚀 How to Run Locally</h2>
<ol>
  <li>Clone the repository:
    <pre>git clone https://github.com/pratiksutar841/[your-repo-name].git</pre>
  </li>
  <li>Navigate into the project directory:
    <pre>cd [your-repo-name]</pre>
  </li>
  <li>Install required dependencies:
    <pre>pip install -r requirements.txt</pre>
  </li>
  <li>Run the main script:
    <pre>python main.py</pre>
  </li>
</ol>

<hr>

<h2>📊 Output Summary</h2>
<ul>
  <li>Coach-wise split video clips</li>
  <li>Frames extracted and stored per coach folder</li>
  <li>Optional annotated images showing detected doors</li>
  <li>Coach count and frame-wise PDF/HTML report (if implemented)</li>
</ul>

<hr>

<h2>🙋‍♂️ Author</h2>
<p>
<b>Pratik Sutar</b><br>
B.Tech in Computer Science & Engineering (Data Science)<br>
GitHub: <a href="https://github.com/pratiksutar841">pratiksutar841</a><br>
LinkedIn: <a href="https://www.linkedin.com/in/pratik-sutar-/">Pratik Sutar</a>
</p>

</body>
</html>
