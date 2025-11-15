import flet as ft

def main(page: ft.Page):
    """Pagina con sfondo diviso in due colori che occupano tutta la finestra."""
    page.title = "Background diviso"
    page.padding = 0
    page.spacing = 0
    page.window.maximized = True 
    page.window.alignment = ft.alignment.center
    page.bgcolor = ft.Colors.GREY_400
    w = page.width or 1200
    black_circle = ft.Container(
            width=7,
            height=7,
            bgcolor=ft.Colors.BLACK,
            border_radius=7 / 2 
        )
    
    
    

    def build_ui_pc():
        LM = 50          
        LM_LG = 80       
        LXL = 150        
        RM = int(max(16, w * 0.05))           
        IMG_H = int(min(300, max(120, w * 0.25)))
        TEXT_W1 = int(min(1100, max(300, int(w * 0.7))))
        TEXT_W2 = int(min(1300, max(300, int(w * 0.9))))
        TEXT_W3 = int(min(1100, max(300, int(w * 0.5))))
        H1 = 40
        H2 = 30
        P = 18
        PFW = int(w * 0.4)
        TOP_OFFSET = int(max(60, w * 0.12))
        PFLM = 200
        PFTM = 120
        PROFILE_TOP = int(TOP_OFFSET * 0.35)
        RIGHT_COL_TOP = int(TOP_OFFSET * 0.6)
        

        background = ft.Column(
            controls=[
                ft.Container(
                    content = (ft.Row(
                        spacing=20,
                        controls = [
                         ft.Container(
                             content = (ft.Image(
                                                src="Profile Image.png",
                                                border_radius=ft.border_radius.all(15),
                                                fit=ft.ImageFit.CONTAIN,
                                                height=IMG_H,
                                                )),
                             margin=ft.margin.only(bottom=10, left=LM)
                         ),
                         ft.Column(
                         controls = [
                             ft.Container(
                                 content = (
                                     ft.Text("ALESSIO CURCIO", size = H1, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER)
                                 ),
                                 expand = 6,
                                 margin=ft.margin.only(top = PFTM, left=LM)
                             ),
                             ft.Container(
                                 content = (
                                     ft.Text("University student", size = H2, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_700, text_align=ft.TextAlign.CENTER)
                                 ),
                                 margin=ft.margin.only(left=LM),
                                 expand = 4
                             )
                         ],
                         spacing=0
                         ),
                         ft.Container(
                             content=ft.Column(
                                 controls=[
                                     ft.Row(
                                         controls=[
                                             ft.Container(
                                                 content=(ft.Image("Profile.png", height=50, width=50, fit=ft.ImageFit.CONTAIN)),
                                                 margin=ft.margin.only(left=LM_LG, top=PROFILE_TOP),
                                             ),
                                             ft.Container(
                                                 content=(ft.Text("Profile", color=ft.Colors.BLACK, size=30, weight=ft.FontWeight.BOLD)),
                                                 margin=ft.margin.only(top=PROFILE_TOP),
                                             ),
                                         ]
                                     ),
                                     ft.Container(
                                         content=(
                                             ft.Text(
                                                 "Hi, I’m Alessio and I'm currently a 3rd year student at the Sapienza University of Rome in the Faculty of Applied Computer Science and Artificial Intelligence (ACSAI).",
                                                 color=ft.Colors.GREY_700,
                                                 size=22,
                                                 weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD),
                                                 text_align=ft.TextAlign.LEFT,
                                             )
                                         ),
                                         expand=1,
                                         margin=ft.margin.only(left=LM_LG, right=RM, top=10),
                                     ),
                                     ft.Container(                                             
                                                 bgcolor="#deb887",
                                                 content=ft.TextButton(
                                                 "Download CV",
                                                 icon="Download",
                                                 style=ft.ButtonStyle(color=ft.Colors.BLACK, text_style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20),shadow_color=ft.Colors.BLACK, padding=ft.padding.all(5)),
                                                 on_click=lambda e: page.launch_url("Alessio Curcio CV.pdf"),
                                             ),
                                             border_radius=ft.border_radius.all(13),
                                         padding=ft.padding.all(3),
                                         alignment=ft.alignment.bottom_right,
                                         margin=ft.margin.only(right=100, top=50),
                                         expand=1
                                     ),
                                 ],
                             ),
                             margin=ft.margin.only(left=LM, top=PFTM*0.2, bottom = PFTM*0.4),
                             expand=1,
                         ),
                        ],  
                    )
                    ),
                    bgcolor="#deb887", 
                    expand=3,
                    border_radius=ft.border_radius.only(
                        top_left=30, 
                        top_right=30
                    ), 
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content = ft.Container(
                                    content=ft.Text("Skills / Experiences", size=P+12, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT),
                                    margin=ft.margin.only(right=20, left = 20)
                                ),
                                margin = ft.margin.only(left = LM, top = 40),
                                bgcolor="#deb887",
                                border_radius=ft.border_radius.all(10),
                            ),
                            ft.Container(
                                content=ft.Text("Education", size = P+8, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT),
                                margin=ft.margin.only(left = LM)
                            ),
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        content=ft.Row(
                                            controls=[
                                                black_circle,
                                                ft.Container(
                                                    content=ft.Text(
                                                        "Graduated from Liceo Scientifico Statale 'Vito Volterra' in 2023 with a score of 98/100, specializing in applied computer science and mathematics.",
                                                        size=P+2,
                                                        weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD),
                                                        color=ft.Colors.GREY_700,
                                                        text_align=ft.TextAlign.LEFT,
                                                    ),
                                                    expand=1,
                                                )
                                            ],
                                        ),
                                        margin=ft.margin.only(left=LM, right=RM),
                                    ),
                                    ft.Container(
                                        content=ft.Row(
                                            controls=[
                                                black_circle,
                                                ft.Container(
                                                    content=ft.Text(
                                                        "Currently pursuing a Bachelor's degree in Applied Computer Science and Artificial Intelligence at Sapienza University of Rome, with an expected graduation date of 2026. Relevant coursework includes Data Structures and Algorithms, Databases, Computer Networks, Web Programming, Operating Systems, and Artificial Intelligence.",
                                                        size=P+2,
                                                        weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD),
                                                        color=ft.Colors.GREY_700,
                                                        text_align=ft.TextAlign.LEFT,
                                                    ),
                                                    expand=1,
                                                )
                                            ]
                                        ),
                                        margin=ft.margin.only(left=LM, right=RM),
                                    ),
                                ]
                            ),
                            ft.Container(
                                content=ft.Text("Coding  Skill", size = 25, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT),
                                margin=ft.margin.only(left = LM, top = 20)
                            ),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Container(
                                            content=ft.Text(
                                                "Programming experience in Python (main programming language), C++, C, R, Java and html/javascript",
                                                size=18,
                                                weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD),
                                                color=ft.Colors.GREY_700,
                                                text_align=ft.TextAlign.LEFT,
                                            ),
                                            margin=ft.margin.only(left=LM),
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Container(
                                                    content=black_circle,
                                                    margin=ft.margin.only(left=LM),
                                                ),
                                                ft.Text(
                                                    "I scored 30 and 30 cum laude in the programming exams at university (Python and Java exams).",
                                                    size=18,
                                                    weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD),
                                                    color=ft.Colors.GREY_700,
                                                    text_align=ft.TextAlign.LEFT,
                                                ),
                                            ]
                                        ),
                                    ]
                                ),
                                expand=1,
                            ),
                            ft.Container(
                                content=ft.Text("Competition", size = 25, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT),
                                margin=ft.margin.only(left=LM, right=RM),
                            ),
                            ft.Container(
                                content = ft.Text("Participated in several programming and mathematical competitions at national, achieving notable rankings.", size = 18, weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD), color=ft.Colors.GREY_700, text_align=ft.TextAlign.LEFT),
                                margin = ft.margin.only(left = LM)
                            ),
                            ft.Container(
                                content = ft.Row(
                                controls = [
                                    black_circle,
                                    ft.Text("Mathematics, Computer Science and Problem Solving Olympics reaching regional stages;", size = 18, weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD), color=ft.Colors.GREY_700, text_align=ft.TextAlign.LEFT)
                                ]
                            ),
                                margin = ft.margin.only(left = LM)
                            ),
                            ft.Container(
                                content = ft.Row(
                                controls = [
                                    black_circle,
                                    ft.Text("Bocconi University’s game reaching national stages;", size = 18, weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD), color=ft.Colors.GREY_700, text_align=ft.TextAlign.LEFT)
                                ]
                            ),
                                margin = ft.margin.only(left = LM)
                            ),
                            ft.Container(
                                content = ft.Row(
                                controls = [
                                    black_circle,
                                    ft.Text("Obtaining the maximum score in the TeraBebras competition;", size = 18, weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD), color=ft.Colors.GREY_700, text_align=ft.TextAlign.LEFT)
                                ]
                            ),
                                margin = ft.margin.only(left = LM)
                            ),
                            ft.Container(
                                content = ft.Row(
                                controls = [
                                    black_circle,
                                    ft.Text("Cybersecurity competition passing the qualification stage", size = 18, weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD), color=ft.Colors.GREY_700, text_align=ft.TextAlign.LEFT)
                                ]
                            ),
                                margin = ft.margin.only(left = LM)
                            ),
                            ft.Container(
                                content=ft.Text("Projects / Activities", size = 25, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT),
                                margin=ft.margin.only(left = LM, top = 20)
                            ),
                            ft.Container(
                                content = ft.Text("Activities in association with IBM, Ericsson, Fondazione Mondo Digitale, Tor Vergata University. We have addressed topics as block programming for animation, chat bots for costumer services and conducted research utilizing big data analytics to construct datadriven personality profiles for public figures using IBM web tools and servers, digital lab ai and robotics.",
                                                   size = 18, weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD), color=ft.Colors.GREY_700, text_align=ft.TextAlign.LEFT, ),
                                margin=ft.margin.only(left = LM),
                                expand=1,
                            ),
                            ft.Container(
                                content=ft.Text("Certification / Experiences", size = 25, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT),
                                margin=ft.margin.only(left = LM, top = 20)
                            ),
                            ft.Container(
                                content = ft.Row(
                                controls = [
                                    black_circle,
                                    ft.Text("Achieved a B2 level certification in English;", size = 18, weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD), color=ft.Colors.GREY_700, text_align=ft.TextAlign.LEFT)
                                ]
                            ),
                                margin = ft.margin.only(left = LM)
                            ),
                            ft.Container(
                                content = ft.Row(
                                controls = [
                                    black_circle,
                                    ft.Text("Participated in a study abroad program in Oxford;", size = 18, weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD), color=ft.Colors.GREY_700, text_align=ft.TextAlign.LEFT)
                                ]
                            ),
                                margin = ft.margin.only(left = LM)
                            ),
                            ft.Container(
                                content = ft.Row(
                                controls = [
                                    black_circle,
                                    ft.Text("Currently pursuing a degree program entirely taught in English.", size = 18, weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD), color=ft.Colors.GREY_700, text_align=ft.TextAlign.LEFT)
                                ]
                            ),
                                margin = ft.margin.only(left = LM, right=RM),
                            ),
                            ft.Container(
                                content=ft.Text("University faculty program", size = 25, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT),
                                margin=ft.margin.only(left = LM, top = 20)
                            ),
                            ft.Container(
                                content = ft.Row(
                                    controls = [
                                        black_circle,
                                        ft.Container(
                                            content = ft.Text(
                                                "Activities in association with IBM, Ericsson, Fondazione Mondo Digitale, Tor Vergata University. We have addressed topics as block programming for animation, chat bots for costumer services and conducted research utilizing big data analytics to construct datadriven personality profiles for public figures using IBM web tools and servers, digital lab ai and robotics.",
                                                size = P+2, weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD), color=ft.Colors.GREY_700, text_align=ft.TextAlign.LEFT,
                                            ),
                                            expand=1,
                                        ),
                                    ]
                                ),
                                margin = ft.margin.only(left = LM, right=RM),
                            ),
                            ft.Container(
                                content = ft.Row(
                                controls = [
                                    black_circle,
                                    ft.Text("Attended a certified Html course at my university.", size = 18, weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD), color=ft.Colors.GREY_700, text_align=ft.TextAlign.LEFT)
                                ]
                            ),
                                margin = ft.margin.only(left = LM)
                            ),
                            ft.Container(
                                content = ft.Container(
                                    content = ft.Text("Contacts", size = 30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER),
                                    margin=ft.margin.only(right=20, left = 20)
                                ),
                                bgcolor = "#deb887",
                                margin=ft.margin.only(left = 50, top = 20),
                                border_radius=ft.border_radius.all(10)
                            ),
                            ft.Container(
                                content = ft.Row(
                                    controls = [
                                        ft.Image("Home.png", height = 45, fit=ft.ImageFit.COVER),
                                        ft.Text("  Rome, Ciampino", size = 18, weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD), color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT)
                                    ]
                                ),
                                margin = ft.margin.only(left = LM, top = 20)
                                
                            ),
                            ft.Container(
                                content = ft.Row(
                                    controls = [
                                        ft.Image("Phone.png", height = 35, fit=ft.ImageFit.COVER),
                                        ft.Text("  +39 3711712524", size = 18, weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD), color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT)
                                    ]
                                ),
                                margin = ft.margin.only(left = LM, top = 20)
                                
                            ),
                            ft.Container(
                                content = ft.Row(
                                controls = [
                                    ft.Image("Email.jpg", height = 35, fit=ft.ImageFit.COVER),
                                    ft.Text("  alessio.curcio04@gmail.com", size = 18, weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD), color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT)
                                ]
                            ),
                                margin = ft.margin.only(left = LM, top = 20)
                            ),
                            ft.Container(
                                content = ft.Row(
                                controls = [
                                    ft.Image("linkedin.png", height = 35, fit=ft.ImageFit.COVER),
                                    ft.TextButton("Alessio Curcio", on_click= lambda e: page.launch_url("https://www.linkedin.com/in/alessio-curcio-7787b935a"),style=ft.ButtonStyle(color=ft.Colors.BLACK, text_style=ft.TextStyle(weight=ft.FontWeight.BOLD, size = 18)) )
                                ]
                            ),
                                margin = ft.margin.only(left = LM, top = 20)
                            ),
                            ft.Container(
                                content = ft.Row(
                                controls = [
                                    ft.Image("Github.png", height = 35, fit=ft.ImageFit.COVER),
                                    ft.TextButton("Crucio104", on_click= lambda e: page.launch_url("https://github.com/Crucio104"),style=ft.ButtonStyle(color=ft.Colors.BLACK, text_style=ft.TextStyle(weight=ft.FontWeight.BOLD, size = 18)), )
                                ]
                            ),
                                margin = ft.margin.only(left = LM, top = 20, bottom = 60)
                            ),
      
                        ],
                        expand=0
                    ),
                    
                    bgcolor=ft.Colors.WHITE,
                    expand=7,
                    border_radius=ft.border_radius.only(
                        bottom_left=30,
                        bottom_right=30
                    ),
                ),
            ],
            expand = False,
            spacing=-1
        )


        frame = ft.Container(
            bgcolor=ft.Colors.BLACK,
            border_radius=ft.border_radius.all(40),
            padding=ft.padding.all(8),
            alignment=ft.alignment.center,
            content=ft.Container(
                content=background,
                bgcolor=None,
            ),
            margin=ft.margin.only(top=30, bottom=30, right=30, left=30),
            shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.BLACK, offset=ft.Offset(0, 0)),
        )

        return ft.ListView(
            controls=[
                ft.Container(
                    content=frame,
                    alignment=ft.alignment.center,
                )
            ],
            expand=True,
        )

    def on_resize(e):
        try:
            try:
                while page.controls:
                    page.controls.pop()
            except Exception:
                pass

            if page.width is None:
                page.add(build_ui_pc())
            elif page.width < 1200:
                page.add(build_ui_mobile())
            else:
                page.add(build_ui_pc())
        except Exception:
            pass
        page.update()

    def build_ui_mobile():
        w = page.width or 380
        container_w = int(min(420, max(300, w - 32)))
        IMG_H = int(min(160, max(90, w * 0.28)))
        header = ft.Container(
            content = ft.Column(
            controls=[
                ft.Container(
                    content=ft.Image(src="Profile Image.png", height=IMG_H*1.3, fit=ft.ImageFit.FIT_HEIGHT, border_radius=ft.border_radius.all(15)),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=12),
                    padding = ft.padding.all(1),
                ),
                ft.Container(
                    content=ft.Text("ALESSIO CURCIO", size=21, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLACK),
                    alignment=ft.alignment.center
                    ),
                ft.Container(
                    content = ft.Text("University student", size=16, color=ft.Colors.GREY_700, text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD),
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=ft.Text("Hi, I’m Alessio and I'm currently a 3rd year student at the Sapienza University of Rome in the Faculty of Applied Computer Science and Artificial Intelligence (ACSAI).",
                                    text_align=ft.TextAlign.CENTER, size=14, color=ft.Colors.GREY_700, weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD)),
                    margin=ft.margin.only(left=12, right=12, top=6),
                ),
                ft.Container(
                    content=ft.Button("Download CV", icon="Download", on_click=lambda e: page.launch_url("Alessio Curcio CV.pdf"), style=ft.ButtonStyle(bgcolor="#deb887", color=ft.Colors.BLACK, text_style=ft.TextStyle(weight=ft.FontWeight.BOLD))),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=8, bottom=8),
                ),
            ],
        ),
            bgcolor = "#deb887",
            border_radius=ft.border_radius.only(top_left=20, top_right=20),
        )
        
            

        body = ft.Container(
            content = ft.Column(
            controls=[
                ft.Container(content=ft.Text("Skills / Experiences", weight=ft.FontWeight.BOLD, size=16, color=ft.Colors.BLACK),
                             margin=ft.margin.only(left=12, top=20, right=12), bgcolor = "#deb887", padding=ft.padding.all(6), border_radius=ft.border_radius.all(10),
                             ),
                ft.Container(
                                content=ft.Text("Education", size = 14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT),
                                margin=ft.margin.only(left=18, top=6, right = 18)
                            ),
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        content=ft.Row(
                                            controls=[
                                                black_circle,
                                                ft.Container(
                                                    content=ft.Text(
                                                        "Graduated from Liceo Scientifico Statale 'Vito Volterra' in 2023 with a score of 98/100, specializing in applied computer science and mathematics.",
                                                        size=12,
                                                        weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD),
                                                        color=ft.Colors.GREY_700,
                                                        text_align=ft.TextAlign.LEFT,
                                                    ),
                                                    expand=1,
                                                )
                                            ],
                                        ),
                                        margin=ft.margin.only(left=18, top=6, right = 18)
                                    ),
                                    ft.Container(
                                        content=ft.Row(
                                            controls=[
                                                black_circle,
                                                ft.Container(
                                                    content=ft.Text(
                                                        "Currently pursuing a Bachelor's degree in Applied Computer Science and Artificial Intelligence at Sapienza University of Rome, with an expected graduation date of 2026. Relevant coursework includes Data Structures and Algorithms, Databases, Computer Networks, Web Programming, Operating Systems, and Artificial Intelligence.",
                                                        size=12,
                                                        weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD),
                                                        color=ft.Colors.GREY_700,
                                                        text_align=ft.TextAlign.LEFT,
                                                    ),
                                                    expand=1,
                                                )
                                            ]
                                        ),
                                        margin=ft.margin.only(left=18, top=6, right = 18)
                                    ),
                                ]
                            ),
                            ft.Container(
                                content=ft.Text("Coding  Skill", size = 14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT),
                                margin=ft.margin.only(left=18, top=6, right = 18)
                            ),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Container(
                                            content=ft.Text(
                                                "Programming experience in Python (main programming language), C++, C, R, Java and html/javascript",
                                                size=12,
                                                weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD),
                                                color=ft.Colors.GREY_700,
                                                text_align=ft.TextAlign.LEFT,
                                            ),
                                            margin=ft.margin.only(left=18, top=6, right = 18)
                                        ),
                                        ft.Container(
                                        content=ft.Row(
                                            controls=[
                                                black_circle,
                                                ft.Container(
                                                    content=ft.Text(
                                                        "I scored 30 and 30 cum laude in the programming exams at university (Python and Java exams).",
                                                        size=12,
                                                        weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD),
                                                        color=ft.Colors.GREY_700,
                                                        text_align=ft.TextAlign.LEFT,
                                                    ),
                                                    expand=1,
                                                )
                                            ],
                                        ),
                                        margin=ft.margin.only(left=18, top=6, right = 18)
                                    ),
                                        
                                    ]
                                ),
                                expand=1,
                            ),
                            ft.Container(
                                content=ft.Text("Competition", size = 14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT),
                                margin=ft.margin.only(left=18, top=6, right = 18)
                            ),
                            ft.Container(
                                        content=ft.Row(
                                            controls=[
                                                black_circle,
                                                ft.Container(
                                                    content=ft.Text(
                                                        "Participated in several programming and mathematical competitions at national, achieving notable rankings.",
                                                        size=12,
                                                        weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD),
                                                        color=ft.Colors.GREY_700,
                                                        text_align=ft.TextAlign.LEFT,
                                                    ),
                                                    expand=1,
                                                ),
                                            ]
                                        ),
                                        margin=ft.margin.only(left=18, top=6, right = 18),
                                        ),
                            ft.Container(
                                        content=ft.Row(
                                            controls=[
                                                black_circle,
                                                ft.Container(
                                                    content=ft.Text(
                                                        "Mathematics, Computer Science and Problem Solving Olympics reaching regional stages;",
                                                        size=12,
                                                        weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD),
                                                        color=ft.Colors.GREY_700,
                                                        text_align=ft.TextAlign.LEFT,
                                                    ),
                                                    expand=1,
                                                ),
                                            ]
                                        ),
                                        margin=ft.margin.only(left=18, top=6, right = 18),
                                        ),
                            ft.Container(
                                        content=ft.Row(
                                            controls=[
                                                black_circle,
                                                ft.Container(
                                                    content=ft.Text(
                                                        "Bocconi University’s game reaching national stages;",
                                                        size=12,
                                                        weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD),
                                                        color=ft.Colors.GREY_700,
                                                        text_align=ft.TextAlign.LEFT,
                                                    ),
                                                    expand=1,
                                                ),
                                            ]
                                        ),
                                        margin=ft.margin.only(left=18, top=6, right = 18),
                                        ),
                            ft.Container(
                                        content=ft.Row(
                                            controls=[
                                                black_circle,
                                                ft.Container(
                                                    content=ft.Text(
                                                        "Obtaining the maximum score in the TeraBebras competition;",
                                                        size=12,
                                                        weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD),
                                                        color=ft.Colors.GREY_700,
                                                        text_align=ft.TextAlign.LEFT,
                                                    ),
                                                    expand=1,
                                                ),
                                            ]
                                        ),
                                        margin=ft.margin.only(left=18, top=6, right = 18),
                                        ),
                                                
                            ft.Container(
                                        content=ft.Row(
                                            controls=[
                                                black_circle,
                                                ft.Container(
                                                    content=ft.Text(
                                                        "Cybersecurity competition passing the qualification stage",
                                                        size=12,
                                                        weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD),
                                                        color=ft.Colors.GREY_700,
                                                        text_align=ft.TextAlign.LEFT,
                                                    ),
                                                    expand=1,
                                                ),
                                            ]
                                        ),
                                        margin=ft.margin.only(left=18, top=6, right = 18),
                                        ),
                            ft.Container(
                                content=ft.Text("Projects / Activities", size = 14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT),
                                margin=ft.margin.only(left=18, top=6, right = 18)
                            ),
                            ft.Container(
                                content = ft.Text("Activities in association with IBM, Ericsson, Fondazione Mondo Digitale, Tor Vergata University. We have addressed topics as block programming for animation, chat bots for costumer services and conducted research utilizing big data analytics to construct datadriven personality profiles for public figures using IBM web tools and servers, digital lab ai and robotics.",
                                                   size = 12, weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD), color=ft.Colors.GREY_700, text_align=ft.TextAlign.LEFT, ),
                                expand=1,
                                margin=ft.margin.only(left=18, top=6, right = 18)
                            ),
                            ft.Container(
                                content=ft.Text("Certification / Experiences", size = 14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT),
                                margin=ft.margin.only(left=18, top=6, right = 18)
                            ),
                            ft.Container(
                                        content=ft.Row(
                                            controls=[
                                                black_circle,
                                                ft.Container(
                                                    content=ft.Text(
                                                        "Achieved a B2 level certification in English;",
                                                        size=12,
                                                        weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD),
                                                        color=ft.Colors.GREY_700,
                                                        text_align=ft.TextAlign.LEFT,
                                                    ),
                                                    expand=1,
                                                ),
                                            ]
                                        ),
                                        margin=ft.margin.only(left=18, top=6, right = 18),
                                        ),
                            ft.Container(
                                        content=ft.Row(
                                            controls=[
                                                black_circle,
                                                ft.Container(
                                                    content=ft.Text(
                                                        "Participated in a study abroad program in Oxford;",
                                                        size=12,
                                                        weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD),
                                                        color=ft.Colors.GREY_700,
                                                        text_align=ft.TextAlign.LEFT,
                                                    ),
                                                    expand=1,
                                                ),
                                            ]
                                        ),
                                        margin=ft.margin.only(left=18, top=6, right = 18),
                            ),
                            ft.Container(
                                        content=ft.Row(
                                            controls=[
                                                black_circle,
                                                ft.Container(
                                                    content=ft.Text(
                                                        "Currently pursuing a degree program entirely taught in English.",
                                                        size=12,
                                                        weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD),
                                                        color=ft.Colors.GREY_700,
                                                        text_align=ft.TextAlign.LEFT,
                                                    ),
                                                    expand=1,
                                                ),
                                            ]),
                                        margin=ft.margin.only(left=18, top=6, right = 18),
                                        ),

                            ft.Container(
                                content=ft.Text("University faculty program", size = 14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT),
                                margin=ft.margin.only(left=18, top=6, right = 18)
                            ),
                            ft.Container(
                                content = ft.Row(
                                    controls = [
                                        black_circle,
                                        ft.Container(
                                            content = ft.Text(
                                                "Activities in association with IBM, Ericsson, Fondazione Mondo Digitale, Tor Vergata University. We have addressed topics as block programming for animation, chat bots for costumer services and conducted research utilizing big data analytics to construct datadriven personality profiles for public figures using IBM web tools and servers, digital lab ai and robotics.",
                                                size = 12, weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD), color=ft.Colors.GREY_700, text_align=ft.TextAlign.LEFT,
                                            ),
                                            expand=1,
                                        ),
                                    ]
                                ),
                                margin=ft.margin.only(left=18, top=6, right = 18)
                            ),
                            ft.Container(
                                content = ft.Row(
                                controls = [
                                    black_circle,
                                    ft.Text("Attended a certified Html course at my university.", size = 12, weight=getattr(ft.FontWeight, "W_600", ft.FontWeight.BOLD), color=ft.Colors.GREY_700, text_align=ft.TextAlign.LEFT)
                                ]
                            ),
                                margin=ft.margin.only(left=18, top=6, right = 18)
                            ),
                ft.Container(content=ft.Text("Contacts", weight=ft.FontWeight.BOLD, size=16, color=ft.Colors.BLACK),
                             margin=ft.margin.only(left=12, top=6, right=12), bgcolor = "#deb887", padding=ft.padding.all(6), border_radius=ft.border_radius.all(10)
                             ),
                ft.Container(
                    content=ft.Column(
                            controls=[
                                ft.Text("Rome, Ciampino", size=12, color=ft.Colors.BLACK, weight=ft.FontWeight.W_600),
                                ft.Text("+39 3711712524", size=12, color=ft.Colors.BLACK, weight=ft.FontWeight.W_600),
                                ft.Text("alessio.curcio@example.com", size=12, color=ft.Colors.BLACK, weight=ft.FontWeight.W_600)
                            ]
                    ),
                    margin=ft.margin.only(left=18, top=6, right = 18)
                ),
                ft.Container(
                                content = ft.Row(
                                controls = [
                                    ft.Image("linkedin.png", height = 12, fit=ft.ImageFit.COVER),
                                    ft.TextButton("Alessio Curcio", on_click= lambda e: page.launch_url("https://www.linkedin.com/in/alessio-curcio-7787b935a"),style=ft.ButtonStyle(color=ft.Colors.BLACK, text_style=ft.TextStyle(weight=ft.FontWeight.W_600, size = 12)) )
                                ]
                            ),
                                margin=ft.margin.only(left=18)
                            ),
                            ft.Container(
                                content = ft.Row(
                                controls = [
                                    ft.Image("Github.png", height = 12, fit=ft.ImageFit.COVER),
                                    ft.TextButton("Crucio104", on_click= lambda e: page.launch_url("https://github.com/Crucio104"),style=ft.ButtonStyle(color=ft.Colors.BLACK, text_style=ft.TextStyle(weight=ft.FontWeight.W_600, size = 12)), )
                                ]
                            ),
                                margin=ft.margin.only(left=18, bottom = 25)
                            ),

                            
                
            ],
            
   
        ),
        
            bgcolor = ft.Colors.WHITE,
            border_radius=ft.border_radius.only(bottom_left=20, bottom_right=20),
        )

        frame_mobile = ft.Container(
            bgcolor=ft.Colors.BLACK,
            content=ft.Column(controls=[header, body],
                              spacing = 0
                              ),
            width=container_w,
            padding=ft.padding.all(6),
            border_radius=ft.border_radius.all(25),
            alignment=ft.alignment.center,
            shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.BLACK, offset=ft.Offset(0, 0)),
            margin=ft.margin.only(top=30, bottom=30)
        )

        return ft.ListView(controls=[ft.Row(controls=[frame_mobile], alignment=ft.MainAxisAlignment.CENTER)], expand=True)
    page.on_resized = on_resize

    if page.width is None:
        page.add(build_ui_pc())
    elif page.width < 1200:
        page.add(build_ui_mobile())
    else:
        page.add(build_ui_pc())

if __name__ == "__main__":
    ft.app(target=main)