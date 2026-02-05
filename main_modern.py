"""
Doctor House - AI Medical Diagnosis System
Modern, Professional Medical UI Interface
"""
import tkinter as tk
from tkinter import ttk, font as tkfont
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import backend


class ModernButton(tk.Canvas):
    """Custom modern button with hover effects and animations"""

    def __init__(self, parent, text, command, bg_color="#0EA5E9", hover_color="#0284C7",
                 text_color="white", width=200, height=50, **kwargs):
        super().__init__(parent, width=width, height=height, highlightthickness=0, **kwargs)
        self.command = command
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.width = width
        self.height = height
        self.text = text

        self.config(bg=parent.cget('bg'))
        self.draw_button(self.bg_color)

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)

    def draw_button(self, color):
        """Draw rounded rectangle button"""
        self.delete("all")
        # Rounded rectangle
        radius = 12
        self.create_oval(0, 0, radius * 2, radius * 2, fill=color, outline="")
        self.create_oval(self.width - radius * 2, 0, self.width, radius * 2, fill=color, outline="")
        self.create_oval(0, self.height - radius * 2, radius * 2, self.height, fill=color, outline="")
        self.create_oval(self.width - radius * 2, self.height - radius * 2, self.width, self.height, fill=color,
                         outline="")
        self.create_rectangle(radius, 0, self.width - radius, self.height, fill=color, outline="")
        self.create_rectangle(0, radius, self.width, self.height - radius, fill=color, outline="")

        # Text
        self.create_text(self.width / 2, self.height / 2, text=self.text, fill=self.text_color,
                         font=("Helvetica", 13, "bold"))

    def on_enter(self, _event):
        """Hover effect"""
        self.draw_button(self.hover_color)

    def on_leave(self, _event):
        """Leave hover"""
        self.draw_button(self.bg_color)

    def on_click(self, _event):
        """Execute command"""
        if self.command:
            self.command()


class DoctorHouseApp:
    """Modern Medical Diagnosis Application

    Instance Attributes:
        - root: Main application window
        - widgets: Dictionary storing all UI elements
        - animation_id: Current animation timer ID
    """

    root: tk.Tk
    widgets: dict
    animation_id: str | None

    def __init__(self, my_root: tk.Tk) -> None:
        """Initialize the modern medical interface"""
        self.root = my_root
        self.root.title("Doctor House - AI Medical Diagnosis")
        self.root.geometry("1400x900")
        self.widgets = {}
        self.animation_id = None

        # Set up window properties
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", self.toggle_fullscreen)

        # Modern color scheme - Medical Blue & White
        self.colors = {
            'primary': '#0EA5E9',  # Sky Blue
            'primary_dark': '#0284C7',  # Darker Sky Blue
            'secondary': '#8B5CF6',  # Purple
            'background': '#F8FAFC',  # Almost White
            'surface': '#FFFFFF',  # Pure White
            'surface_variant': '#F1F5F9',  # Light Gray
            'text': '#0F172A',  # Almost Black
            'text_secondary': '#64748B',  # Gray
            'success': '#10B981',  # Green
            'error': '#EF4444',  # Red
            'border': '#E2E8F0'  # Light Border
        }

        self.root.config(bg=self.colors['background'])

        # Configure grid
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=2)
        self.root.rowconfigure(0, weight=1)

        self.setup_styles()
        self.create_header()
        self.create_main_layout()

    def setup_styles(self):
        """Configure modern TTK styles"""
        style = ttk.Style(self.root)
        style.theme_use('clam')

        # Configure frames
        style.configure('Card.TFrame', background=self.colors['surface'], relief='flat')
        style.configure('TFrame', background=self.colors['background'])

        # Configure labels
        style.configure('Title.TLabel',
                        background=self.colors['surface'],
                        foreground=self.colors['text'],
                        font=('Helvetica', 32, 'bold'))

        style.configure('Subtitle.TLabel',
                        background=self.colors['surface'],
                        foreground=self.colors['text_secondary'],
                        font=('Helvetica', 14))

        style.configure('Header.TLabel',
                        background=self.colors['surface'],
                        foreground=self.colors['text'],
                        font=('Helvetica', 16, 'bold'))

        style.configure('Body.TLabel',
                        background=self.colors['surface'],
                        foreground=self.colors['text'],
                        font=('Helvetica', 12))

    def create_header(self):
        """Create application header with branding"""
        header = tk.Frame(self.root, bg=self.colors['surface'], height=100)
        header.grid(row=0, column=0, columnspan=2, sticky="ew")
        header.grid_propagate(False)

        # Medical cross icon (using text)
        icon_frame = tk.Frame(header, bg=self.colors['primary'], width=70, height=70)
        icon_frame.place(x=40, y=15)

        icon_label = tk.Label(icon_frame, text="✚", font=("Arial", 32),
                              bg=self.colors['primary'], fg="white")
        icon_label.place(relx=0.5, rely=0.5, anchor="center")

        # Title
        title_label = tk.Label(header, text="Doctor House",
                               font=("Helvetica", 28, "bold"),
                               bg=self.colors['surface'],
                               fg=self.colors['text'])
        title_label.place(x=130, y=20)

        # Subtitle
        subtitle_label = tk.Label(header, text="AI-Powered Medical Diagnosis System",
                                  font=("Helvetica", 12),
                                  bg=self.colors['surface'],
                                  fg=self.colors['text_secondary'])
        subtitle_label.place(x=130, y=55)

        # Separator line
        separator = tk.Frame(header, bg=self.colors['border'], height=1)
        separator.place(x=0, y=99, relwidth=1)

    def create_main_layout(self):
        """Create the main application layout"""
        # Left Panel - Symptom Search
        left_container = tk.Frame(self.root, bg=self.colors['background'])
        left_container.grid(row=1, column=0, sticky="nsew", padx=30, pady=20)

        self.create_search_panel(left_container)

        # Right Panel - Selected Symptoms
        right_container = tk.Frame(self.root, bg=self.colors['background'])
        right_container.grid(row=1, column=1, sticky="nsew", padx=(0, 30), pady=20)

        self.create_symptoms_panel(right_container)

    def create_search_panel(self, parent):
        """Create the symptom search card"""
        # Card frame with shadow effect
        card = tk.Frame(parent, bg=self.colors['surface'], relief='flat', bd=0)
        card.pack(fill=tk.BOTH, expand=True)

        # Add subtle shadow
        shadow = tk.Frame(parent, bg='#CBD5E1', relief='flat')
        shadow.place(in_=card, x=4, y=4, relwidth=1, relheight=1)
        card.lift()

        # Content padding
        content = tk.Frame(card, bg=self.colors['surface'])
        content.pack(fill=tk.BOTH, expand=True, padx=40, pady=30)

        # Header
        header = tk.Label(content, text="Search Symptoms",
                          font=("Helvetica", 22, "bold"),
                          bg=self.colors['surface'],
                          fg=self.colors['text'])
        header.pack(anchor="w", pady=(0, 10))

        # Description
        desc = tk.Label(content,
                        text="Start typing to search for symptoms. Click to add to your selection.",
                        font=("Helvetica", 11),
                        bg=self.colors['surface'],
                        fg=self.colors['text_secondary'],
                        wraplength=500,
                        justify="left")
        desc.pack(anchor="w", pady=(0, 25))

        # Search input frame
        search_frame = tk.Frame(content, bg=self.colors['surface_variant'],
                                highlightbackground=self.colors['border'],
                                highlightthickness=2, highlightcolor=self.colors['primary'])
        search_frame.pack(fill=tk.X, pady=(0, 15))

        # Search icon
        search_icon = tk.Label(search_frame, text="🔍", font=("Arial", 16),
                               bg=self.colors['surface_variant'])
        search_icon.pack(side=tk.LEFT, padx=(15, 10), pady=12)

        # Entry field
        self.widgets["entry"] = tk.Entry(search_frame,
                                         font=("Helvetica", 13),
                                         bg=self.colors['surface_variant'],
                                         fg=self.colors['text'],
                                         relief='flat',
                                         insertbackground=self.colors['primary'])
        self.widgets["entry"].pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=12, padx=(0, 15))
        self.widgets["entry"].bind("<KeyRelease>", self.update_list)
        self.widgets["entry"].bind("<FocusIn>", self.show_dropdown)

        # Dropdown frame
        self.widgets["dropdown_frame"] = tk.Frame(self.root,
                                                  bg=self.colors['surface'],
                                                  relief='flat',
                                                  highlightbackground=self.colors['border'],
                                                  highlightthickness=1)

        # Listbox with modern styling
        self.widgets["listbox"] = tk.Listbox(self.widgets["dropdown_frame"],
                                             height=8,
                                             bg=self.colors['surface'],
                                             fg=self.colors['text'],
                                             selectbackground=self.colors['primary'],
                                             selectforeground='white',
                                             font=("Helvetica", 12),
                                             relief='flat',
                                             highlightthickness=0,
                                             activestyle='none')
        self.widgets["listbox"].pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.widgets["listbox"].bind("<ButtonRelease-1>", self.select_option)

        # Info card
        info_card = tk.Frame(content, bg=self.colors['surface_variant'],
                             highlightbackground=self.colors['border'], highlightthickness=1)
        info_card.pack(fill=tk.X, pady=20)

        info_icon = tk.Label(info_card, text="ℹ️", font=("Arial", 14),
                             bg=self.colors['surface_variant'])
        info_icon.pack(side=tk.LEFT, padx=15, pady=15)

        info_text = tk.Label(info_card,
                             text="Select multiple symptoms for more accurate diagnosis results.",
                             font=("Helvetica", 11),
                             bg=self.colors['surface_variant'],
                             fg=self.colors['text_secondary'],
                             wraplength=450,
                             justify="left")
        info_text.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=15, padx=(0, 15))

        # Bind click outside
        self.root.bind('<Button-1>', self.hide_dropdown)

    def create_symptoms_panel(self, parent):
        """Create selected symptoms panel"""
        # Card frame
        card = tk.Frame(parent, bg=self.colors['surface'], relief='flat')
        card.pack(fill=tk.BOTH, expand=True)

        # Shadow
        shadow = tk.Frame(parent, bg='#CBD5E1', relief='flat')
        shadow.place(in_=card, x=4, y=4, relwidth=1, relheight=1)
        card.lift()

        # Content
        content = tk.Frame(card, bg=self.colors['surface'])
        content.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

        # Header
        header_frame = tk.Frame(content, bg=self.colors['surface'])
        header_frame.pack(fill=tk.X, pady=(0, 20))

        header = tk.Label(header_frame, text="Selected Symptoms",
                          font=("Helvetica", 22, "bold"),
                          bg=self.colors['surface'],
                          fg=self.colors['text'])
        header.pack(side=tk.LEFT)

        # Count badge
        self.widgets["count_badge"] = tk.Label(header_frame, text="0",
                                               font=("Helvetica", 12, "bold"),
                                               bg=self.colors['primary'],
                                               fg="white",
                                               padx=10, pady=3)
        self.widgets["count_badge"].pack(side=tk.LEFT, padx=15)

        # Symptoms list frame
        list_container = tk.Frame(content, bg=self.colors['surface_variant'],
                                  highlightbackground=self.colors['border'],
                                  highlightthickness=1)
        list_container.pack(fill=tk.BOTH, expand=True, pady=(0, 20))

        # Custom listbox with modern styling
        self.widgets["lst_box"] = tk.Listbox(list_container,
                                             bg=self.colors['surface'],
                                             fg=self.colors['text'],
                                             font=("Helvetica", 13),
                                             relief='flat',
                                             highlightthickness=0,
                                             selectbackground=self.colors['surface_variant'],
                                             selectforeground=self.colors['text'],
                                             activestyle='none')

        scrollbar = tk.Scrollbar(list_container, command=self.widgets["lst_box"].yview)
        self.widgets["lst_box"].config(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.widgets["lst_box"].pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Bind selection change to update count
        self.widgets["lst_box"].bind('<<ListboxSelect>>', lambda e: self.update_symptom_count())

        # Action buttons
        button_frame = tk.Frame(content, bg=self.colors['surface'])
        button_frame.pack(fill=tk.X)

        # Clear button
        clear_btn = ModernButton(button_frame, "Clear All", self.clear_lst_box,
                                 bg_color=self.colors['surface_variant'],
                                 hover_color='#E2E8F0',
                                 text_color=self.colors['text'],
                                 height=50)
        clear_btn.pack(side=tk.LEFT, padx=(0, 10))

        # Diagnose button
        diagnose_btn = ModernButton(button_frame, "Get Diagnosis", self.check_diagnosis,
                                    bg_color=self.colors['primary'],
                                    hover_color=self.colors['primary_dark'],
                                    width=250,
                                    height=50)
        diagnose_btn.pack(side=tk.LEFT, expand=True, fill=tk.X)

        # Error label
        self.widgets["label_error"] = tk.Label(content, text="",
                                               font=("Helvetica", 11),
                                               bg=self.colors['surface'],
                                               fg=self.colors['error'])
        self.widgets["label_error"].pack(pady=(15, 0))

    def update_symptom_count(self):
        """Update symptom count badge"""
        count = self.widgets["lst_box"].size()
        self.widgets["count_badge"].config(text=str(count))

    def toggle_fullscreen(self, _event: tk.Event = None) -> None:
        """Toggle fullscreen mode"""
        is_fullscreen = self.root.attributes('-fullscreen')
        self.root.attributes('-fullscreen', not is_fullscreen)

    def update_list(self, _event: tk.Event = None) -> None:
        """Update dropdown list based on user input"""
        typed = self.widgets["entry"].get().lower()
        self.widgets["listbox"].delete(0, tk.END)
        filtered = [symptom for symptom in SYMPTOM_OPTIONS if typed in symptom.lower()]

        if filtered and typed:
            for item in filtered[:10]:  # Limit to 10 items
                self.widgets["listbox"].insert(tk.END, item)

            # Position dropdown
            entry_widget = self.widgets["entry"]
            x_pos = entry_widget.winfo_rootx() - self.root.winfo_rootx()
            y_pos = entry_widget.winfo_rooty() - self.root.winfo_rooty() + entry_widget.winfo_height() + 5
            width = entry_widget.winfo_width() + 80

            self.widgets["dropdown_frame"].place(x=x_pos, y=y_pos, width=width)
        else:
            self.widgets["dropdown_frame"].place_forget()

    def show_dropdown(self, _event: tk.Event = None) -> None:
        """Show dropdown on focus"""
        self.update_list()

    def select_option(self, _event: tk.Event) -> None:
        """Add selected symptom to list"""
        if not self.widgets["listbox"].curselection():
            return

        selected = self.widgets["listbox"].get(self.widgets["listbox"].curselection())

        # Check if already added
        current_symptoms = self.widgets["lst_box"].get(0, tk.END)
        if selected not in current_symptoms:
            self.widgets["lst_box"].insert(tk.END, selected)
            self.update_symptom_count()

        self.widgets["entry"].delete(0, tk.END)
        self.widgets["dropdown_frame"].place_forget()

    def hide_dropdown(self, event: tk.Event) -> None:
        """Hide dropdown when clicking outside"""
        if event.widget not in (self.widgets["entry"], self.widgets["listbox"]):
            self.widgets["dropdown_frame"].place_forget()

    def clear_lst_box(self) -> None:
        """Clear selected symptoms"""
        self.widgets["lst_box"].delete(0, tk.END)
        self.update_symptom_count()

    def check_diagnosis(self) -> None:
        """Process diagnosis request"""
        patient_symptoms = self.widgets["lst_box"].get(0, tk.END)

        if patient_symptoms:
            result = backend.calculate_potential_disease(DIAGNOSIS_GRAPH, patient_symptoms)
            DiagnosisWindow(self.root, result)
            self.clear_lst_box()
        else:
            self.widgets["label_error"].config(text="⚠️ Please select at least one symptom")
            self.root.after(3000, lambda: self.widgets["label_error"].config(text=""))


class DiagnosisWindow:
    """Modern diagnosis results window"""

    pop_up: tk.Toplevel
    elements: dict
    colors: dict

    def __init__(self, parent: tk.Tk, data: dict) -> None:
        """Create modern diagnosis window"""
        self.pop_up = tk.Toplevel(parent)
        self.pop_up.title("Diagnosis Results - Doctor House")
        self.pop_up.geometry("1400x900")
        self.elements = {}

        # Color scheme
        self.colors = {
            'primary': '#0EA5E9',
            'primary_dark': '#0284C7',
            'secondary': '#8B5CF6',
            'background': '#F8FAFC',
            'surface': '#FFFFFF',
            'surface_variant': '#F1F5F9',
            'text': '#0F172A',
            'text_secondary': '#64748B',
            'success': '#10B981',
            'error': '#EF4444',
            'warning': '#F59E0B',
            'border': '#E2E8F0'
        }

        self.pop_up.attributes('-fullscreen', True)
        self.pop_up.bind("<Escape>", self.toggle_fullscreen)
        self.pop_up.config(bg=self.colors['background'])

        self.create_diagnosis_layout(data)

    def create_diagnosis_layout(self, data: dict):
        """Create the diagnosis results layout"""
        # Header
        header = tk.Frame(self.pop_up, bg=self.colors['surface'], height=100)
        header.pack(fill=tk.X)

        header_content = tk.Frame(header, bg=self.colors['surface'])
        header_content.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)

        # Back button
        back_btn = tk.Label(header_content, text="← Back",
                            font=("Helvetica", 12),
                            bg=self.colors['surface'],
                            fg=self.colors['primary'],
                            cursor="hand2")
        back_btn.pack(side=tk.LEFT)
        back_btn.bind("<Button-1>", lambda e: self.pop_up.destroy())

        # Title
        title = tk.Label(header_content, text="Diagnosis Results",
                         font=("Helvetica", 28, "bold"),
                         bg=self.colors['surface'],
                         fg=self.colors['text'])
        title.pack(side=tk.LEFT, padx=30)

        # Separator
        separator = tk.Frame(self.pop_up, bg=self.colors['border'], height=1)
        separator.pack(fill=tk.X)

        # Main content container
        content = tk.Frame(self.pop_up, bg=self.colors['background'])
        content.pack(fill=tk.BOTH, expand=True, padx=40, pady=30)

        # Configure grid
        content.columnconfigure(0, weight=1)
        content.rowconfigure(0, weight=1)
        content.rowconfigure(1, weight=1)

        # Chart section
        self.create_modern_chart(content, data)

        # Disease info section
        self.create_disease_info_section(content, data)

    def create_modern_chart(self, parent, data: dict):
        """Create modern visualization chart"""
        chart_card = tk.Frame(parent, bg=self.colors['surface'])
        chart_card.grid(row=0, column=0, sticky="nsew", pady=(0, 20))

        # Shadow
        shadow = tk.Frame(parent, bg='#CBD5E1')
        shadow.place(in_=chart_card, x=4, y=4, relwidth=1, relheight=1)
        chart_card.lift()

        # Header
        chart_header = tk.Frame(chart_card, bg=self.colors['surface'])
        chart_header.pack(fill=tk.X, padx=30, pady=(25, 15))

        tk.Label(chart_header, text="Probability Analysis",
                 font=("Helvetica", 20, "bold"),
                 bg=self.colors['surface'],
                 fg=self.colors['text']).pack(side=tk.LEFT)

        tk.Label(chart_header, text="Based on selected symptoms",
                 font=("Helvetica", 11),
                 bg=self.colors['surface'],
                 fg=self.colors['text_secondary']).pack(side=tk.LEFT, padx=15)

        # Chart
        fig = Figure(figsize=(12, 4), dpi=100, facecolor=self.colors['surface'])
        ax = fig.add_subplot(111)

        categories = list(data.keys())
        values = list(data.values())

        # Create gradient colors
        colors_list = []
        for i, val in enumerate(values):
            if val >= 40:
                colors_list.append('#EF4444')  # Red for high probability
            elif val >= 25:
                colors_list.append('#F59E0B')  # Orange for medium
            else:
                colors_list.append('#10B981')  # Green for low

        bars = ax.barh(categories, values, color=colors_list, height=0.6)

        # Add value labels
        for i, (bar, val) in enumerate(zip(bars, values)):
            ax.text(val + 1, i, f'{val:.1f}%', va='center',
                    font=dict(size=11, weight='bold'), color=self.colors['text'])

        ax.set_xlabel('Probability (%)', fontsize=12, color=self.colors['text_secondary'])
        ax.set_xlim(0, 105)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color(self.colors['border'])
        ax.spines['bottom'].set_color(self.colors['border'])
        ax.tick_params(colors=self.colors['text'])
        ax.set_facecolor(self.colors['surface'])
        fig.tight_layout(pad=2)

        canvas = FigureCanvasTkAgg(fig, master=chart_card)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=30, pady=(0, 20))

    def create_disease_info_section(self, parent, data: dict):
        """Create disease information section"""
        info_card = tk.Frame(parent, bg=self.colors['surface'])
        info_card.grid(row=1, column=0, sticky="nsew")

        # Shadow
        shadow = tk.Frame(parent, bg='#CBD5E1')
        shadow.place(in_=info_card, x=4, y=4, relwidth=1, relheight=1)
        info_card.lift()

        # Header
        info_header = tk.Frame(info_card, bg=self.colors['surface'])
        info_header.pack(fill=tk.X, padx=30, pady=(25, 20))

        tk.Label(info_header, text="Disease Information",
                 font=("Helvetica", 20, "bold"),
                 bg=self.colors['surface'],
                 fg=self.colors['text']).pack(side=tk.LEFT)

        # Disease tabs
        tabs_frame = tk.Frame(info_card, bg=self.colors['surface'])
        tabs_frame.pack(fill=tk.X, padx=30, pady=(0, 20))

        self.elements["disease_buttons"] = []
        for i, (disease, prob) in enumerate(data.items()):
            btn_frame = tk.Frame(tabs_frame, bg=self.colors['surface_variant'],
                                 highlightbackground=self.colors['border'],
                                 highlightthickness=1)
            btn_frame.pack(side=tk.LEFT, padx=(0, 10), pady=5)

            btn = tk.Label(btn_frame, text=f"{disease}\n{prob:.1f}%",
                           font=("Helvetica", 11, "bold"),
                           bg=self.colors['surface_variant'],
                           fg=self.colors['text'],
                           padx=20, pady=12,
                           cursor="hand2")
            btn.pack()

            btn.bind("<Button-1>", lambda e, d=disease: self.show_disease_info(d))
            btn.bind("<Enter>", lambda e, b=btn_frame: b.config(
                highlightbackground=self.colors['primary'], highlightthickness=2))
            btn.bind("<Leave>", lambda e, b=btn_frame: b.config(
                highlightbackground=self.colors['border'], highlightthickness=1))

            self.elements["disease_buttons"].append((btn_frame, btn))

        # Info display area
        info_container = tk.Frame(info_card, bg=self.colors['surface_variant'],
                                  highlightbackground=self.colors['border'],
                                  highlightthickness=1)
        info_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=(0, 30))

        self.elements["info_text"] = tk.Text(info_container,
                                             wrap=tk.WORD,
                                             font=("Helvetica", 12),
                                             bg=self.colors['surface'],
                                             fg=self.colors['text'],
                                             relief='flat',
                                             padx=25,
                                             pady=25,
                                             spacing1=5,
                                             spacing3=5)

        scrollbar = tk.Scrollbar(info_container, command=self.elements["info_text"].yview)
        self.elements["info_text"].config(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.elements["info_text"].pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configure text tags
        self.elements["info_text"].tag_configure("title", font=("Helvetica", 18, "bold"),
                                                 foreground=self.colors['text'], spacing1=10)
        self.elements["info_text"].tag_configure("heading", font=("Helvetica", 14, "bold"),
                                                 foreground=self.colors['primary'], spacing1=15)
        self.elements["info_text"].tag_configure("body", font=("Helvetica", 12),
                                                 foreground=self.colors['text'], spacing1=5)
        self.elements["info_text"].tag_configure("advice", font=("Helvetica", 12),
                                                 foreground=self.colors['text'], lmargin1=30, lmargin2=30)

        # Show first disease by default
        if data:
            first_disease = list(data.keys())[0]
            self.show_disease_info(first_disease)

    def show_disease_info(self, disease: str):
        """Display information for selected disease"""
        info_text = self.elements["info_text"]
        info_text.config(state='normal')
        info_text.delete(1.0, tk.END)

        # Title
        info_text.insert(tk.END, f"{disease}\n", "title")

        # Description
        info_text.insert(tk.END, "\n📋 Description\n", "heading")
        info_text.insert(tk.END, f"{DISEASE_DICT[disease].description}\n", "body")

        # Precautions
        info_text.insert(tk.END, "\n💊 Recommended Precautions\n", "heading")
        for i, advice in enumerate(DISEASE_DICT[disease].advice, 1):
            info_text.insert(tk.END, f"\n{i}. {advice}", "advice")

        # Disclaimer
        info_text.insert(tk.END, "\n\n⚠️ Medical Disclaimer\n", "heading")
        disclaimer = ("This is an AI-based prediction tool for educational purposes only. "
                      "Always consult with a qualified healthcare professional for accurate "
                      "diagnosis and treatment. Do not use this as a substitute for professional "
                      "medical advice.")
        info_text.insert(tk.END, disclaimer, "body")

        info_text.config(state='disabled')

        # Highlight selected disease button
        for btn_frame, btn in self.elements["disease_buttons"]:
            if disease in btn.cget("text"):
                btn_frame.config(bg=self.colors['primary'],
                                 highlightbackground=self.colors['primary'])
                btn.config(bg=self.colors['primary'], fg='white')
            else:
                btn_frame.config(bg=self.colors['surface_variant'],
                                 highlightbackground=self.colors['border'])
                btn.config(bg=self.colors['surface_variant'],
                           fg=self.colors['text'])

    def toggle_fullscreen(self, _event: tk.Event = None) -> None:
        """Toggle fullscreen mode"""
        is_fullscreen = self.pop_up.attributes('-fullscreen')
        self.pop_up.attributes('-fullscreen', not is_fullscreen)


# Load data
DIAGNOSIS_GRAPH, SYMPTOMS_LIST, NAME_TO_DISEASE_MAP = backend.load_diagnosis_graph(
    'Symptom-severity.csv',
    'dataset.csv',
    'symptom_Description.csv',
    'symptom_precaution.csv')
SYMPTOM_OPTIONS = sorted(SYMPTOMS_LIST.copy())
DISEASE_DICT = NAME_TO_DISEASE_MAP

if __name__ == '__main__':
    root = tk.Tk()
    app = DoctorHouseApp(root)
    root.mainloop()
