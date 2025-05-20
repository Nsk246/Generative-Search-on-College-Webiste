import reflex as rx



dots: dict={
    "@keyframes dots":{
        "0%": {"background_position": "0 0"},
        "100%": {"background_position": "40px 40px"}, 
    },
    "animation": "dots 4s linear infinite alternate-reverse both",

}
wave: dict={
    "@keyframes wave":{
        "0%": {"transformer": "roatate(45deg)"},
        "100%": {"transformer": "roatate(-15deg)"}, 
    },
    "animation": "wave 0.8s cubic-bezier(0.25,0.46,0.45.0.94) infinite alternate-reverse both",

}



css: dict={
       "app":{
        "_dark":{
            "bg":"#15171b"
        }
    },

 "header":{
        "width":"100%",
        "height":"50px",
          "padding":[
            "0rem 1rem",
            "0rem 1rem",
            "0rem 1rem"
            "0rem 8rem"
            "0rem 8rem"
        ],
        "transition":"all 550ms ease",

 },
   "main":{
        "property":{
        "width":"100%",
        "height":"84vh",
        "padding":"15rem 30rem",
        "align _items":"center",
        "justify_content":"start",
        }
        }
    }





class Header:
    def __init__(self):
        self.header : rx.Hstack = rx.hstack(style=css.get("header"))
        self.email : rx.Hstack =rx.chakra.hstack(
            #rx.chakra.box(rx.chakra.icon(tag="download",_dark={"color":"rgba(255,255,255,0.5"})),
              rx.box(
                rx.text(
                    "campusquest@gmail.com",opacity=0.3,_dark={"color":"rgba(255,255,255,0.5)"}
                )
            ),
            align_items="center",
            justify_content="center",
        )
        self.theme: rx.Theme = rx.theme(appearance="dark" ,has_background=True)
        
    def compile_component(self):
        return [self.email,rx.spacer(),self.theme]
    def build(self):
        self.header.children=self.compile_component()
        return self.header   

class Main:
    def __init__(self):
        self.box: rx.chakra.Box=rx.chakra.box(width="100%")

        self.name: rx.chakra.Hstack = rx.chakra.hstack(
            
            rx.chakra.heading(
                "‎ ‎ ‎ The Campus Quest",
                font_size=["2rem","2.85rem","4rem","5rem","5rem"],
                font_weight="900",
                     _dark={
                    "background":"linear-gradient(to right,#ele1e1, #757575)",
                    #"background_clip": "text",

                }
               

            ),
        )
        self.badge_stack_max: rx.Hstack=rx.hstack(spacing="3")
        self.badge_stack_min: rx.Vstack=rx.vstack(spacing="3")
        titles: list= ["Powered by LARGE LANGUAGE MODEL","College of Engineering Perumon","Generative Search ON COLLEGE DATA"]
        self.badge_stack_max.children = [self.create_badges(title) for title in titles]
        self.badge_stack_min.children = [self.create_badges(title) for title in titles]
        self.btn : rx.chakra.button = rx.center(rx.button("sdfghj",opacity=0),rx.button("sdfghj",opacity=0),rx.button("sdfghj",opacity=0),rx.button("shj",opacity=0),rx.button("sdhj",opacity=0),rx.button("sghj",opacity=0),rx.button("Start Search",on_click=rx.redirect("/search")))
        
    def create_badges(self,title:str):
        return rx.chakra.badge(
            title,
            variant="solid",
            padding=[
                "0.15rem 0.35rem",
                "0.15rem 0.35rem",
                "0.15rem 1rem",
                "0.15rem 1rem",
                "0.15rem 1rem",
            ]
        )
    def compile_desktop_component(self):
           return rx.tablet_and_desktop(
            rx.vstack(
                self.name,
                self.badge_stack_max,
                rx.button("sdfghj",opacity=0),
                self.btn,
                style=css.get("main").get("property"),

            )
        )
    def build(self):
        self.box.children=[self.compile_desktop_component()]
        return self.box


@rx.page(route="/")

def landing()->rx.Component:
    header : object =Header().build()
    main : object=Main().build()

    return rx.vstack(
        header,
        main,
         _light={
            "background":"radial-gradient(circle,rgba(0,0,0,0.35) 1px,transparent 1px)",
            "background_size":"25px 25px",
        },

        background="radial-gradient(circle, rgba(255,255,255,0.09) 1px, transparent 1px)",
        background_size="25px 25px",
        style=dots

    )

app = rx.App(style=css.get("app"))
app.compile()