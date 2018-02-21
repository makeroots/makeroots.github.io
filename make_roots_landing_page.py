from yattag import Doc
from pprint import pprint


doc, tag, text = Doc().tagtext()

with tag('html', lang="en", klass="gr__blackrockdigital_github_io"):

    # Header
    with tag('head'):
        doc.stag('meta', name="viewport", content="width=device-width, initial-scale=1, shrink-to-fit=no")
        doc.stag('meta', name="description", content="My website!")
        doc.stag('meta', name="author", content="Aidan Low")
        with tag('title'): text('MakeRoots')
        with tag('script', src="https://use.fontawesome.com/cc09d94a65.js"): pass # Font-Awesome
        doc.stag('link', href="CSSFiles/bootstrap.min.css", rel="stylesheet") # Bootstrap CSS
        doc.stag('link', href="CSSFiles/custom.css", rel="stylesheet") # Custom CSS
        with tag('script', src="JSFiles/overlay.js"): pass # Custom JS
        with tag('script', src="JSFiles/divheights.js"): pass # Custom JS

    # Body
    with tag('body', id='page-top', data_gr_c_s_loaded="true"):
        # Navigation
        with tag('div', klass="navbar navbar-fixed-left"):
            with tag('div', klass="main-container"):
                with tag('div', klass="fixer-container"):
                    with tag('ul', klass='nav navbar-nav'):
                        def make_link(LINK):
                            with tag('li'):
                                with tag('a', klass="nav-link active", href=LINK):
                                    with tag('i', klass="fa fa-circle", aria_hidden="true"): pass
                        make_link("./index.html#page1")
                        make_link("./index.html#page2")
                        make_link("./index.html#page3")
                        make_link("./index.html#page4")
                        make_link("./index.html#page5")

        # Page 1
        with tag('section', id="page1", klass="screener"):
            with tag('div', klass='bg bg1'): pass
            with tag('div', klass='container section-content'):
                with tag('div', klass='row padder'):
                    with tag('div', klass="col-md-12 mx-auto"):
                        with tag('h1', klass='greentext'):
                            text('MakeRoots')
                        with tag('h1'):
                            text('Grow something good.')
                        doc.stag('br')
                        doc.stag('br')
                        with tag('p', klass="lead"):
                            text('We are building a space to connect passionate people and nonprofits that are tackling our world\'s biggest challenges.')

        # Page 2
        with tag('section', id="page2", klass="screener"):
            with tag('div', klass='bg bg2'): pass
            with tag('div', klass='container section-content'):
                with tag('div', klass='row padder'):
                    with tag('div', klass="col-md-12 mx-auto"):
                        with tag('h1'):
                            text("What's the problem with philanthropy?")
                        doc.stag('br')
                def make_page_2_list_item(NUMBER, TITLE, CONTENT):
                    with tag('div', klass='row'):
                        with tag('div', klass='col-md-offset-1 col-md-3 col-sm-2',
                                 style="border-bottom: 4px solid green"):
                            with tag('p', klass="lead", style='text-align:right; margin: 0; margin-top: 20px;'):
                                text(NUMBER)
                        with tag('div', klass='col-md-8 col-sm-10'):
                            with tag('h2'):
                                text(TITLE)
                            with tag('p', klass="lead"):
                                text(CONTENT)
                make_page_2_list_item("1.", "Lorem ipsum dolor sit amet.", "Lorem ipsum dolor sit amet.")
                make_page_2_list_item("2.", "Lorem ipsum dolor sit amet.", "Lorem ipsum dolor sit amet.")
                make_page_2_list_item("3.", "Lorem ipsum dolor sit amet.", "Lorem ipsum dolor sit amet.")


        # Page 3
        with tag('section', id="page3", klass="screener"):
            with tag('div', klass='bg bg3'): pass
            with tag('div', klass='container section-content'):
                with tag('div', klass='row padder'):
                    with tag('div', klass="col-md-12 mx-auto"):
                        with tag('h1'):
                            text("Let's change that.")
                        doc.stag('br')
                        with tag('p', klass="lead"):
                            text('Lorem ipsum dolor sit amet.')
                        doc.stag('br')
                        with tag('p', klass="lead"):
                            text('Lorem ipsum dolor sit amet.')

        # Page 4
        with tag('section', id="page4", klass="screener"):
            with tag('div', klass='bg bg4'): pass
            with tag('div', klass='container section-content'):
                with tag('div', klass='row padder'):
                    with tag('div', klass="col-md-12 mx-auto"):
                        with tag('h1', style="color:#BF94E4"):
                            text('Donate your...')
                            doc.stag('br')
                    with tag('div', klass="col-md-5 mx-auto"):
                        def make_page_3_list_item(ITEM):
                            doc.stag('br')
                            with tag('p', klass="lead", style="font-size:30px;"):
                                text(ITEM)
                        make_page_3_list_item('Money.')
                        make_page_3_list_item('Time.')
                        make_page_3_list_item('Creativity.')
                        make_page_3_list_item('Passion.')
                        make_page_3_list_item('Love.')
                        make_page_3_list_item('Anything.')
                    with tag('div', klass="col-md-offset-2 col-md-5 mx-auto"):
                        with tag('p', style="text-align:right;"):
                            text('Lorem ipsum dolor sit amet')

        # Page 5
        with tag('section', id="page5", klass="screener"):
            with tag('div', klass='bg bg5'): pass
            with tag('div', klass='container section-content'):
                with tag('div', klass='row padder'):
                    with tag('div', klass="col-md-12 mx-auto"):
                        with tag('h1', klass="greentext"):
                            text('Tell us what you think.')
                with tag('div', klass='row'):
                    with tag('div', klass='col-md-6 mx-auto'):
                        with tag('p', klass="lead"):
                            doc.stag('br')
                            text('Lorem ipsum dolor sit amet.')
                            doc.stag('br')
                            doc.stag('br')
                        with tag('div', klass="btn btn-lg btn-default", onclick="on()",
                                 style="background-color:#BF94E4; border-color:white; color:white; font-size 20px;"):
                            text('Chat with us!')
                    with tag('div', klass='col-md-6 mx-auto', id='overlay', style="display:none;"):
                        text("I am an email form!")




testing_file = open('index.html', 'w')
processed_string = doc.getvalue()
processed_string = processed_string.replace('aria_hidden', 'aria-hidden')
processed_string = processed_string.replace('data_grc_s_loaded', 'data-gr-c-s-loaded')
processed_string = processed_string.replace('<', '\r<')
testing_file.write(processed_string)
testing_file.close()
