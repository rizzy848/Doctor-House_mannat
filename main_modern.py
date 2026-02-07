"""Doctor House - Modern Medical Diagnosis Interface"""
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import backend


class ModernDoctorHouseApp:
    """Modern medical-themed diagnosis application with professional UI."""

    def __init__(self, my_root: tk.Tk) -> None:
        self.root = my_root
        self.root.title("Doctor House - AI Medical Diagnosis")
        self.root.geometry("1200x800")
        self.widgets = {}

        # Color Palette - Medical Professional Theme
        self.colors = {
            'primary': '#2C3E50',  # Deep blue-gray (professional)
            'secondary': '#3498DB',  # Bright blue (trust/medical)
            'accent': '#E74C3C',  # Red (medical cross)
            'success': '#27AE60',  # Green (health)
            'bg_main': '#ECF0F1',  # Light gray (clean)
            'bg_card': '#FFFFFF',  # White (cards)
            'text_dark': '#2C3E50',  # Dark text
            'text_light': '#7F8C8D',  # Light text
            'border': '#BDC3C7',  # Border gray
            'hover': '#3498DB',  # Hover blue
            'gradient_start': '#667EEA',  # Gradient purple
            'gradient_end': '#764BA2'  # Gradient deep purple
        }

        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", self.toggle_fullscreen)
        self.root.config(bg=self.colors['bg_main'])

        self.setup_styles()
        self.create_header()
        self.create_main_content()
        self.create_footer()

    def setup_styles(self) -> None:
        """Configure modern ttk styles."""
        style = ttk.Style(self.root)
        style.theme_use('clam')

        # Configure Frame styles
        style.configure('Main.TFrame', background=self.colors['bg_main'])
        style.configure('Card.TFrame', background=self.colors['bg_card'], relief='flat')
        style.configure('Header.TFrame', background=self.colors['primary'])

        # Configure Label styles
        style.configure('Title.TLabel',
                        background=self.colors['primary'],
                        foreground='white',
                        font=('Segoe UI', 28, 'bold'))

        style.configure('Subtitle.TLabel',
                        background=self.colors['primary'],
                        foreground='#BDC3C7',
                        font=('Segoe UI', 11))

        style.configure('CardTitle.TLabel',
                        background=self.colors['bg_card'],
                        foreground=self.colors['text_dark'],
                        font=('Segoe UI', 14, 'bold'))

        style.configure('Hint.TLabel',
                        background=self.colors['bg_card'],
                        foreground=self.colors['text_light'],
                        font=('Segoe UI', 9, 'italic'))

        # Configure Button styles
        style.configure('Primary.TButton',
                        background=self.colors['secondary'],
                        foreground='white',
                        borderwidth=0,
                        font=('Segoe UI', 11, 'bold'),
                        padding=(20, 12))

        style.map('Primary.TButton',
                  background=[('active', '#2980B9'), ('pressed', '#21618C')],
                  relief=[('pressed', 'flat')])

        style.configure('Danger.TButton',
                        background=self.colors['accent'],
                        foreground='white',
                        borderwidth=0,
                        font=('Segoe UI', 11, 'bold'),
                        padding=(20, 12))

        style.map('Danger.TButton',
                  background=[('active', '#C0392B')],
                  relief=[('pressed', 'flat')])

        style.configure('Secondary.TButton',
                        background='white',
                        foreground=self.colors['text_dark'],
                        borderwidth=1,
                        font=('Segoe UI', 10),
                        padding=(15, 8))

        style.map('Secondary.TButton',
                  background=[('active', self.colors['bg_main'])],
                  bordercolor=[('active', self.colors['secondary'])])

    def create_header(self) -> None:
        """Create professional header with branding."""
        header_frame = ttk.Frame(self.root, style='Header.TFrame', height=120)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        header_frame.pack_propagate(False)

        # Header content container
        header_content = ttk.Frame(header_frame, style='Header.TFrame')
        header_content.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)

        # Logo section (you can add an image here)
        logo_frame = ttk.Frame(header_content, style='Header.TFrame')
        logo_frame.pack(side=tk.LEFT)

        # Medical cross icon (text-based)
        logo_label = tk.Label(logo_frame,
                              text="⚕",
                              font=('Segoe UI', 48),
                              bg=self.colors['primary'],
                              fg=self.colors['accent'])
        logo_label.pack(side=tk.LEFT, padx=(0, 15))

        # Title section
        title_frame = ttk.Frame(header_content, style='Header.TFrame')
        title_frame.pack(side=tk.LEFT, fill=tk.Y)

        title = ttk.Label(title_frame,
                          text="Doctor House",
                          style='Title.TLabel')
        title.pack(anchor='w')

        subtitle = ttk.Label(title_frame,
                             text="AI-Powered Medical Symptom Analysis",
                             style='Subtitle.TLabel')
        subtitle.pack(anchor='w')

        # Info button (top right)
        info_btn = ttk.Button(header_content,
                              text="ℹ About",
                              style='Secondary.TButton',
                              command=self.show_about)
        info_btn.pack(side=tk.RIGHT, padx=5)

    def create_main_content(self) -> None:
        """Create main content area with modern card layout."""
        # Main container
        main_frame = ttk.Frame(self.root, style='Main.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=30)

        # Configure grid
        main_frame.columnconfigure(0, weight=1, minsize=400)
        main_frame.columnconfigure(1, weight=1, minsize=400)
        main_frame.rowconfigure(0, weight=1)

        # Left Card - Symptom Input
        self.create_symptom_card(main_frame)

        # Right Card - Selected Symptoms
        self.create_selection_card(main_frame)

    def create_symptom_card(self, parent: ttk.Frame) -> None:
        """Create left card for symptom search."""
        # Card container with shadow effect
        card_container = ttk.Frame(parent, style='Main.TFrame')
        card_container.grid(row=0, column=0, sticky='nsew', padx=(0, 15))

        # Shadow frame (visual depth)
        shadow = tk.Frame(card_container, bg='#95A5A6', bd=0)
        shadow.place(x=4, y=4, relwidth=1, relheight=1)

        # Main card
        card = ttk.Frame(card_container, style='Card.TFrame')
        card.place(x=0, y=0, relwidth=1, relheight=1)

        # Card header
        header = ttk.Frame(card, style='Card.TFrame')
        header.pack(fill=tk.X, padx=30, pady=(30, 10))

        card_title = ttk.Label(header,
                               text="🔍 Search Symptoms",
                               style='CardTitle.TLabel')
        card_title.pack(anchor='w')

        hint = ttk.Label(header,
                         text="Type to search from 133 medical symptoms",
                         style='Hint.TLabel')
        hint.pack(anchor='w', pady=(5, 0))

        # Search input container
        input_container = ttk.Frame(card, style='Card.TFrame')
        input_container.pack(fill=tk.X, padx=30, pady=15)

        # Custom styled entry
        self.widgets["entry_frame"] = tk.Frame(input_container,
                                               bg=self.colors['bg_main'],
                                               highlightbackground=self.colors['border'],
                                               highlightthickness=2,
                                               highlightcolor=self.colors['secondary'])
        self.widgets["entry_frame"].pack(fill=tk.X)

        # Search icon
        search_icon = tk.Label(self.widgets["entry_frame"],
                               text="🔎",
                               bg=self.colors['bg_main'],
                               font=('Segoe UI', 14))
        search_icon.pack(side=tk.LEFT, padx=(10, 5))

        self.widgets["entry"] = tk.Entry(self.widgets["entry_frame"],
                                         bg=self.colors['bg_main'],
                                         fg=self.colors['text_dark'],
                                         font=('Segoe UI', 12),
                                         bd=0,
                                         insertbackground=self.colors['secondary'])
        self.widgets["entry"].pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=12)

        self.widgets["entry"].bind("<KeyRelease>", self.update_list)
        self.widgets["entry"].bind("<FocusIn>", self.show_dropdown)
        self.widgets["entry"].bind("<FocusIn>", self.on_entry_focus, add='+')
        self.widgets["entry"].bind("<FocusOut>", self.on_entry_unfocus, add='+')

        # Info section
        info_frame = ttk.Frame(card, style='Card.TFrame')
        info_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

        # Statistics cards
        stats_container = ttk.Frame(info_frame, style='Card.TFrame')
        stats_container.pack(fill=tk.X, pady=10)

        self.create_stat_box(stats_container, "133", "Total Symptoms", 0)
        self.create_stat_box(stats_container, "41", "Diseases", 1)
        self.create_stat_box(stats_container, "AI", "Powered", 2)

        # Instructions
        instructions_frame = ttk.Frame(info_frame, style='Card.TFrame')
        instructions_frame.pack(fill=tk.BOTH, expand=True, pady=20)

        instructions_title = tk.Label(instructions_frame,
                                      text="How to Use:",
                                      bg=self.colors['bg_card'],
                                      fg=self.colors['text_dark'],
                                      font=('Segoe UI', 12, 'bold'))
        instructions_title.pack(anchor='w', pady=(0, 10))

        instructions = [
            "1. Type symptom keywords in the search box",
            "2. Click symptoms from dropdown to select",
            "3. Review selected symptoms on the right",
            "4. Click 'Analyze Symptoms' for diagnosis"
        ]

        for instruction in instructions:
            label = tk.Label(instructions_frame,
                             text=instruction,
                             bg=self.colors['bg_card'],
                             fg=self.colors['text_light'],
                             font=('Segoe UI', 10),
                             anchor='w',
                             justify='left')
            label.pack(anchor='w', pady=3)

        # Dropdown (initially hidden)
        self.widgets["dropdown_frame"] = tk.Frame(self.root,
                                                  bg='white',
                                                  relief=tk.FLAT,
                                                  bd=0,
                                                  highlightbackground=self.colors['border'],
                                                  highlightthickness=1)

        self.widgets["listbox"] = tk.Listbox(self.widgets["dropdown_frame"],
                                             height=8,
                                             bg='white',
                                             fg=self.colors['text_dark'],
                                             selectbackground=self.colors['secondary'],
                                             selectforeground='white',
                                             font=('Segoe UI', 10),
                                             bd=0,
                                             highlightthickness=0,
                                             activestyle='none')
        self.widgets["listbox"].pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.widgets["listbox"].bind("<ButtonRelease-1>", self.select_option)

    def create_selection_card(self, parent: ttk.Frame) -> None:
        """Create right card for selected symptoms."""
        # Card container
        card_container = ttk.Frame(parent, style='Main.TFrame')
        card_container.grid(row=0, column=1, sticky='nsew', padx=(15, 0))

        # Shadow
        shadow = tk.Frame(card_container, bg='#95A5A6', bd=0)
        shadow.place(x=4, y=4, relwidth=1, relheight=1)

        # Main card
        card = ttk.Frame(card_container, style='Card.TFrame')
        card.place(x=0, y=0, relwidth=1, relheight=1)

        # Card header
        header = ttk.Frame(card, style='Card.TFrame')
        header.pack(fill=tk.X, padx=30, pady=(30, 10))

        card_title = ttk.Label(header,
                               text="✓ Selected Symptoms",
                               style='CardTitle.TLabel')
        card_title.pack(anchor='w')

        # Symptom count
        self.widgets["count_label"] = tk.Label(header,
                                               text="0 symptoms selected",
                                               bg=self.colors['bg_card'],
                                               fg=self.colors['text_light'],
                                               font=('Segoe UI', 9))
        self.widgets["count_label"].pack(anchor='w', pady=(5, 0))

        # Selected symptoms list with modern styling
        list_container = ttk.Frame(card, style='Card.TFrame')
        list_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=15)

        # Custom scrollbar
        list_frame = tk.Frame(list_container, bg=self.colors['bg_main'])
        list_frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(list_frame, bg=self.colors['bg_card'])
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.widgets["lst_box"] = tk.Listbox(list_frame,
                                             bg=self.colors['bg_main'],
                                             fg=self.colors['text_dark'],
                                             font=('Segoe UI', 11),
                                             bd=0,
                                             highlightthickness=0,
                                             selectbackground=self.colors['secondary'],
                                             selectforeground='white',
                                             yscrollcommand=scrollbar.set,
                                             activestyle='none')
        self.widgets["lst_box"].pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.widgets["lst_box"].yview)

        # Action buttons
        button_frame = ttk.Frame(card, style='Card.TFrame')
        button_frame.pack(fill=tk.X, padx=30, pady=(10, 30))

        self.widgets["btn_clear"] = ttk.Button(button_frame,
                                               text="🗑 Clear All",
                                               style='Secondary.TButton',
                                               command=self.clear_lst_box)
        self.widgets["btn_clear"].pack(fill=tk.X, pady=(0, 10))

        self.widgets["btn_submit"] = ttk.Button(button_frame,
                                                text="🔬 Analyze Symptoms",
                                                style='Primary.TButton',
                                                command=self.check_diagnosis)
        self.widgets["btn_submit"].pack(fill=tk.X)

        # Error label
        self.widgets["label_error"] = tk.Label(button_frame,
                                               text="",
                                               bg=self.colors['bg_card'],
                                               fg=self.colors['accent'],
                                               font=('Segoe UI', 10, 'bold'))
        self.widgets["label_error"].pack(pady=(10, 0))

    def create_stat_box(self, parent: ttk.Frame, value: str, label: str, column: int) -> None:
        """Create a statistics display box."""
        stat_frame = tk.Frame(parent,
                              bg=self.colors['bg_main'],
                              highlightbackground=self.colors['border'],
                              highlightthickness=1)
        stat_frame.grid(row=0, column=column, sticky='ew', padx=5)
        parent.columnconfigure(column, weight=1)

        value_label = tk.Label(stat_frame,
                               text=value,
                               bg=self.colors['bg_main'],
                               fg=self.colors['secondary'],
                               font=('Segoe UI', 20, 'bold'))
        value_label.pack(pady=(10, 0))

        text_label = tk.Label(stat_frame,
                              text=label,
                              bg=self.colors['bg_main'],
                              fg=self.colors['text_light'],
                              font=('Segoe UI', 9))
        text_label.pack(pady=(0, 10))

    def create_footer(self) -> None:
        """Create footer with disclaimer."""
        footer = tk.Frame(self.root, bg=self.colors['primary'], height=50)
        footer.pack(fill=tk.X, side=tk.BOTTOM)
        footer.pack_propagate(False)

        disclaimer = tk.Label(footer,
                              text="⚠ Disclaimer: This tool is for educational purposes only. Always consult healthcare professionals for medical advice.",
                              bg=self.colors['primary'],
                              fg='#BDC3C7',
                              font=('Segoe UI', 9, 'italic'))
        disclaimer.pack(expand=True)

    def on_entry_focus(self, _event: tk.Event = None) -> None:
        """Visual feedback when entry gets focus."""
        self.widgets["entry_frame"].config(highlightcolor=self.colors['secondary'],
                                           highlightthickness=2)

    def on_entry_unfocus(self, _event: tk.Event = None) -> None:
        """Visual feedback when entry loses focus."""
        self.widgets["entry_frame"].config(highlightcolor=self.colors['border'],
                                           highlightthickness=2)

    def update_symptom_count(self) -> None:
        """Update the symptom count label."""
        count = self.widgets["lst_box"].size()
        text = f"{count} symptom{'s' if count != 1 else ''} selected"
        self.widgets["count_label"].config(text=text)

    def toggle_fullscreen(self, _event: tk.Event = None) -> None:
        """Toggle fullscreen mode."""
        is_fullscreen = self.root.attributes('-fullscreen')
        self.root.attributes('-fullscreen', not is_fullscreen)

    def update_list(self, _event: tk.Event = None) -> None:
        """Update dropdown list based on user input."""
        typed = self.widgets["entry"].get().lower()
        self.widgets["listbox"].delete(0, tk.END)

        filtered = [symptom for symptom in SYMPTOM_OPTIONS if typed in symptom.lower()]

        if filtered and typed:
            for item in filtered:
                self.widgets["listbox"].insert(tk.END, item)

            # Position dropdown below entry
            x_size = self.widgets["entry_frame"].winfo_rootx() - self.root.winfo_rootx()
            y_size = self.widgets["entry_frame"].winfo_rooty() - self.root.winfo_rooty() + \
                     self.widgets["entry_frame"].winfo_height()
            width = self.widgets["entry_frame"].winfo_width()

            self.widgets["dropdown_frame"].place(x=x_size, y=y_size, width=width)
        else:
            self.widgets["dropdown_frame"].place_forget()

    def show_dropdown(self, _event: tk.Event = None) -> None:
        """Show dropdown list."""
        self.update_list()

    def select_option(self, _event: tk.Event) -> None:
        """Select symptom from dropdown."""
        if not self.widgets["listbox"].curselection():
            return

        selected = self.widgets["listbox"].get(self.widgets["listbox"].curselection())

        # Check for duplicates
        current_items = self.widgets["lst_box"].get(0, tk.END)
        if selected not in current_items:
            self.widgets["entry"].delete(0, tk.END)
            self.widgets["lst_box"].insert(tk.END, selected)
            self.update_symptom_count()

        self.widgets["dropdown_frame"].place_forget()

    def hide_dropdown(self, event: tk.Event) -> None:
        """Hide dropdown when clicking outside."""
        if event.widget not in (self.widgets["entry"], self.widgets["listbox"]):
            self.widgets["dropdown_frame"].place_forget()

    def clear_lst_box(self) -> None:
        """Clear selected symptoms."""
        self.widgets["lst_box"].delete(0, tk.END)
        self.update_symptom_count()

    def check_diagnosis(self) -> None:
        """Calculate potential diseases."""
        patient_symptoms = self.widgets["lst_box"].get(0, tk.END)

        if patient_symptoms:
            # Show loading state
            self.widgets["btn_submit"].config(text="⏳ Analyzing...", state='disabled')
            self.root.update()

            result = backend.calculate_potential_disease(DIAGNOSIS_GRAPH, patient_symptoms)

            # Reset button
            self.widgets["btn_submit"].config(text="🔬 Analyze Symptoms", state='normal')

            ModernDiagnosisWindow(self.root, result)
            self.clear_lst_box()
        else:
            self.widgets["label_error"].config(text="⚠ Please select at least one symptom")
            self.root.after(3000, lambda: self.widgets["label_error"].config(text=""))

    def show_about(self) -> None:
        """Show about dialog."""
        about_window = tk.Toplevel(self.root)
        about_window.title("About Doctor House")
        about_window.geometry("500x400")
        about_window.config(bg='white')
        about_window.resizable(False, False)

        # Center window
        about_window.update_idletasks()
        x = (about_window.winfo_screenwidth() // 2) - (500 // 2)
        y = (about_window.winfo_screenheight() // 2) - (400 // 2)
        about_window.geometry(f'500x400+{x}+{y}')

        content = tk.Frame(about_window, bg='white')
        content.pack(fill=tk.BOTH, expand=True, padx=40, pady=30)

        title = tk.Label(content,
                         text="Doctor House",
                         bg='white',
                         fg=self.colors['primary'],
                         font=('Segoe UI', 24, 'bold'))
        title.pack(pady=(0, 10))

        version = tk.Label(content,
                           text="Version 2.0 | AI Medical Diagnosis",
                           bg='white',
                           fg=self.colors['text_light'],
                           font=('Segoe UI', 10))
        version.pack()

        separator = tk.Frame(content, bg=self.colors['border'], height=1)
        separator.pack(fill=tk.X, pady=20)

        about_text = """This application uses graph algorithms and 
probability calculations to analyze symptoms 
and predict potential diseases.

Built with Python, featuring:
• 133 medical symptoms
• 41 disease profiles
• Advanced graph algorithms
• Interactive visualizations

For educational purposes only.
Always consult healthcare professionals."""

        text_label = tk.Label(content,
                              text=about_text,
                              bg='white',
                              fg=self.colors['text_dark'],
                              font=('Segoe UI', 10),
                              justify='center')
        text_label.pack(pady=20)

        close_btn = ttk.Button(content,
                               text="Close",
                               style='Primary.TButton',
                               command=about_window.destroy)
        close_btn.pack(pady=10)


class ModernDiagnosisWindow:
    """Modern diagnosis results window."""

    def __init__(self, parent: tk.Tk, data: dict) -> None:
        """Create modern diagnosis window."""
        self.pop_up = tk.Toplevel(parent)
        self.pop_up.title("Diagnosis Results")
        self.pop_up.geometry("1200x800")
        self.elements = {}

        # Color scheme matching main app
        self.colors = {
            'primary': '#2C3E50',
            'secondary': '#3498DB',
            'accent': '#E74C3C',
            'success': '#27AE60',
            'warning': '#F39C12',
            'bg_main': '#ECF0F1',
            'bg_card': '#FFFFFF',
            'text_dark': '#2C3E50',
            'text_light': '#7F8C8D'
        }

        self.pop_up.attributes('-fullscreen', True)
        self.pop_up.bind("<Escape>", self.toggle_fullscreen)
        self.pop_up.config(bg=self.colors['bg_main'])

        self.create_header()
        self.create_results_content(data)
        self.create_footer()

    def create_header(self) -> None:
        """Create results header."""
        header = tk.Frame(self.pop_up, bg=self.colors['primary'], height=100)
        header.pack(fill=tk.X)
        header.pack_propagate(False)

        content = tk.Frame(header, bg=self.colors['primary'])
        content.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)

        title = tk.Label(content,
                         text="📊 Diagnosis Results",
                         bg=self.colors['primary'],
                         fg='white',
                         font=('Segoe UI', 24, 'bold'))
        title.pack(side=tk.LEFT)

        close_btn = tk.Button(content,
                              text="✕ Close",
                              bg=self.colors['accent'],
                              fg='white',
                              font=('Segoe UI', 11, 'bold'),
                              bd=0,
                              padx=20,
                              pady=10,
                              cursor='hand2',
                              command=self.pop_up.destroy)
        close_btn.pack(side=tk.RIGHT)

    def create_results_content(self, data: dict) -> None:
        """Create main results content."""
        main_frame = tk.Frame(self.pop_up, bg=self.colors['bg_main'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=30)

        # Configure grid
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)

        # Left: Chart
        self.create_chart_panel(main_frame, data)

        # Right: Details
        self.create_details_panel(main_frame, data)

    def create_chart_panel(self, parent: tk.Frame, data: dict) -> None:
        """Create chart visualization panel."""
        # Card container
        card_container = tk.Frame(parent, bg=self.colors['bg_main'])
        card_container.grid(row=0, column=0, sticky='nsew', padx=(0, 15))

        # Shadow
        shadow = tk.Frame(card_container, bg='#95A5A6')
        shadow.place(x=4, y=4, relwidth=1, relheight=1)

        # Card
        card = tk.Frame(card_container, bg=self.colors['bg_card'])
        card.place(x=0, y=0, relwidth=1, relheight=1)

        # Title
        header = tk.Frame(card, bg=self.colors['bg_card'])
        header.pack(fill=tk.X, padx=30, pady=(30, 10))

        title = tk.Label(header,
                         text="Disease Probability Analysis",
                         bg=self.colors['bg_card'],
                         fg=self.colors['text_dark'],
                         font=('Segoe UI', 16, 'bold'))
        title.pack(anchor='w')

        subtitle = tk.Label(header,
                            text="Based on your selected symptoms",
                            bg=self.colors['bg_card'],
                            fg=self.colors['text_light'],
                            font=('Segoe UI', 10))
        subtitle.pack(anchor='w')

        # Chart
        chart_frame = tk.Frame(card, bg=self.colors['bg_card'])
        chart_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        fig = Figure(figsize=(6, 6), dpi=100, facecolor=self.colors['bg_card'])
        ax = fig.add_subplot(111)

        categories = list(data.keys())
        values = list(data.values())

        # Color gradient based on probability
        colors_list = []
        for val in values:
            if val >= 40:
                colors_list.append(self.colors['accent'])
            elif val >= 25:
                colors_list.append(self.colors['warning'])
            else:
                colors_list.append(self.colors['secondary'])

        bars = ax.barh(categories, values, color=colors_list, edgecolor='white', linewidth=2)

        # Add value labels
        for i, (bar, val) in enumerate(zip(bars, values)):
            width = bar.get_width()
            ax.text(width + 1, bar.get_y() + bar.get_height() / 2,
                    f'{val:.1f}%',
                    ha='left', va='center',
                    fontsize=10, fontweight='bold',
                    color=self.colors['text_dark'])

        ax.set_xlabel('Probability (%)', fontsize=11, fontweight='bold', color=self.colors['text_dark'])
        ax.set_title('Likelihood Assessment', fontsize=13, fontweight='bold', pad=20,
                     color=self.colors['text_dark'])
        ax.set_xlim(0, 105)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(axis='x', alpha=0.3, linestyle='--')

        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def create_details_panel(self, parent: tk.Frame, data: dict) -> None:
        """Create disease details panel."""
        # Card container
        card_container = tk.Frame(parent, bg=self.colors['bg_main'])
        card_container.grid(row=0, column=1, sticky='nsew', padx=(15, 0))

        # Shadow
        shadow = tk.Frame(card_container, bg='#95A5A6')
        shadow.place(x=4, y=4, relwidth=1, relheight=1)

        # Card
        card = tk.Frame(card_container, bg=self.colors['bg_card'])
        card.place(x=0, y=0, relwidth=1, relheight=1)

        # Header
        header = tk.Frame(card, bg=self.colors['bg_card'])
        header.pack(fill=tk.X, padx=30, pady=(30, 10))

        title = tk.Label(header,
                         text="Disease Information",
                         bg=self.colors['bg_card'],
                         fg=self.colors['text_dark'],
                         font=('Segoe UI', 16, 'bold'))
        title.pack(anchor='w')

        subtitle = tk.Label(header,
                            text="Select a disease to view details",
                            bg=self.colors['bg_card'],
                            fg=self.colors['text_light'],
                            font=('Segoe UI', 10))
        subtitle.pack(anchor='w')

        # Disease buttons
        button_container = tk.Frame(card, bg=self.colors['bg_card'])
        button_container.pack(fill=tk.X, padx=30, pady=15)

        for i, (disease, prob) in enumerate(data.items()):
            # Color based on probability
            if prob >= 40:
                bg_color = self.colors['accent']
            elif prob >= 25:
                bg_color = self.colors['warning']
            else:
                bg_color = self.colors['secondary']

            btn = tk.Button(button_container,
                            text=f"{disease} ({prob:.1f}%)",
                            bg=bg_color,
                            fg='white',
                            font=('Segoe UI', 11, 'bold'),
                            bd=0,
                            padx=15,
                            pady=12,
                            cursor='hand2',
                            command=lambda d=disease: self.show_info(d))
            btn.pack(fill=tk.X, pady=5)

        # Info display area
        info_container = tk.Frame(card, bg=self.colors['bg_main'])
        info_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=(10, 30))

        # Scrollbar
        scrollbar = tk.Scrollbar(info_container)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.elements["info_text"] = tk.Text(info_container,
                                             wrap=tk.WORD,
                                             bg=self.colors['bg_main'],
                                             fg=self.colors['text_dark'],
                                             font=('Segoe UI', 11),
                                             bd=0,
                                             padx=20,
                                             pady=20,
                                             yscrollcommand=scrollbar.set)
        self.elements["info_text"].pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.elements["info_text"].yview)

        # Initial message
        self.elements["info_text"].insert('1.0',
                                          "👆 Click on a disease above to view detailed information and precautions")
        self.elements["info_text"].config(state='disabled')

    def create_footer(self) -> None:
        """Create footer."""
        footer = tk.Frame(self.pop_up, bg=self.colors['primary'], height=50)
        footer.pack(fill=tk.X)
        footer.pack_propagate(False)

        text = tk.Label(footer,
                        text="⚠ These results are probabilistic estimates. Please consult a healthcare professional for accurate diagnosis.",
                        bg=self.colors['primary'],
                        fg='#BDC3C7',
                        font=('Segoe UI', 9, 'italic'))
        text.pack(expand=True)

    def show_info(self, selected: str) -> None:
        """Display disease information."""
        self.elements["info_text"].config(state='normal')
        self.elements["info_text"].delete('1.0', tk.END)

        # Disease name
        self.elements["info_text"].insert(tk.END, f"{selected}\n", 'title')
        self.elements["info_text"].insert(tk.END, "─" * 60 + "\n\n", 'separator')

        # Description
        self.elements["info_text"].insert(tk.END, "📋 Description\n", 'section')
        self.elements["info_text"].insert(tk.END, f"{DISEASE_DICT[selected].description}\n\n", 'content')

        # Precautions
        self.elements["info_text"].insert(tk.END, "⚕ Recommended Precautions\n", 'section')
        for i, precaution in enumerate(DISEASE_DICT[selected].advice, 1):
            self.elements["info_text"].insert(tk.END, f"  {i}. {precaution}\n", 'content')

        # Configure tags
        self.elements["info_text"].tag_config('title', font=('Segoe UI', 16, 'bold'),
                                              foreground=self.colors['primary'])
        self.elements["info_text"].tag_config('separator', foreground=self.colors['text_light'])
        self.elements["info_text"].tag_config('section', font=('Segoe UI', 12, 'bold'),
                                              foreground=self.colors['secondary'], spacing1=10)
        self.elements["info_text"].tag_config('content', font=('Segoe UI', 11),
                                              spacing1=5)

        self.elements["info_text"].config(state='disabled')

    def toggle_fullscreen(self, _event: tk.Event = None) -> None:
        """Toggle fullscreen."""
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
    app = ModernDoctorHouseApp(root)
    root.mainloop()
