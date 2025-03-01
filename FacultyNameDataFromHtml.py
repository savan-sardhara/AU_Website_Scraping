from bs4 import BeautifulSoup

# HTML content (truncated for brevity; use the full content in practice)
html_content = """
<div class="tab-pane fade" id="faculty" role="tabpanel" aria-labelledby="contact-tab">
    <h2>Faculty <span>profile</span></h2>

    <div class="row" style="margin-bottom:5%;">
        <div class="col-md-4">
            <img src="https://atmiyauni.ac.in/public/facultypro/1733564223.Faculty Emoji File.jpg"
                style="height: 230px; width: 290px;border-radius:10px;">
        </div>

        <div class="col-md-8">
            <h3 style="color: #02215e;margin:0px;">
                <b>Hitendra Nanjibhai Donga</b>
            </h3>
            <br><br>
            <p style="color: #666 !important;font-size: 17px !important;">
                <strong>Professor<br>Ph.D., M.Sc.IT<br>Exp:15</strong>
            </p>
            <hr>
            <p style="height:40px">
                <a style="color: #02215e;">
                    <i class="fa fa-envelope" style="color: #02215e;" aria-hidden="true">
                        hitendra.donga@atmiyauni.ac.in </i>
                </a>
            </p>
        </div>
    </div>
    <div class="row" style="margin-bottom:5%;">
        <div class="col-md-4">
            <img src="https://atmiyauni.ac.in/public/facultypro/1738144427.137.JPG"
                style="height: 230px; width: 290px;border-radius:10px;">
        </div>

        <div class="col-md-8">
            <h3 style="color: #02215e;margin:0px;">
                <b>Vishal Suryakantbhai Vora</b>
            </h3>
            <br><br>
            <p style="color: #666 !important;font-size: 17px !important;">
                <strong>Professor<br>Ph.D., M.E.<br>Exp:19</strong>
            </p>
            <hr>
        </div>
    </div>
</div>
"""

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find and print faculty names
for faculty in soup.find_all('b'):
    print(faculty.get_text())