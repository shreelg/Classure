from flask import Flask, request, render_template
import pandas as pd


app = Flask(__name__)


# Load the CSV data
data = pd.read_csv("Grade Distribution.csv")


# Calculate the average GPA, median GPA, and grade distribution
def calculate_analytics(filtered_data):
   if filtered_data.empty:
       return None, None, None, None, None, None


   avg_gpa = filtered_data['GPA'].mean()
   median_gpa = filtered_data['GPA'].median()
   max_gpa = filtered_data['GPA'].max()
   min_gpa = filtered_data['GPA'].min()
   gpa_std_dev = filtered_data['GPA'].std()


   grade_columns = ['A (%)', 'A- (%)', 'B+ (%)', 'B (%)', 'B- (%)',
                    'C+ (%)', 'C (%)', 'C- (%)', 'D+ (%)', 'D (%)', 'D- (%)', 'F (%)']
   avg_grade_distribution = filtered_data[grade_columns].mean()


   return avg_gpa, median_gpa, max_gpa, min_gpa, gpa_std_dev, avg_grade_distribution


# Home page route
@app.route("/")
def index():
   return render_template("index.html")


# Search route to handle form submission and display results
@app.route("/search", methods=["POST"])
def search():
   course_number = request.form.get("course_number").strip().lower()
   course_title = request.form.get("course_title").strip().lower()


   filtered_data = data.copy()


   if course_number:
       filtered_data = filtered_data[
           filtered_data['Course No.'].astype(str).str.lower().str.contains(course_number, case=False, na=False)
       ]
   if course_title:
       filtered_data = filtered_data[
           filtered_data['Course Title'].str.lower().str.contains(course_title, case=False, na=False)
           
       ]


   avg_gpa, median_gpa, max_gpa, min_gpa, gpa_std_dev, avg_grade_distribution = calculate_analytics(filtered_data)
   rows = len(filtered_data)


   if filtered_data.empty:
       return render_template("search_results.html", avg_gpa=None, median_gpa=None, max_gpa=None, min_gpa=None,
                              gpa_std_dev=None, avg_grade_distribution=None, table=None, rows=0)
   else:
       return render_template(
           "search_results.html",
           avg_gpa=avg_gpa,
           median_gpa=median_gpa,
           max_gpa=max_gpa,
           min_gpa=min_gpa,
           gpa_std_dev=gpa_std_dev,
           avg_grade_distribution=avg_grade_distribution.to_dict(),
           table=filtered_data.to_html(classes='data', header="true", index=False),
           rows=rows
       )


if __name__ == "__main__":
   app.run(debug=True, port=5000)





