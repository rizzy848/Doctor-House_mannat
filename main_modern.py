"""Doctor House - Modern Medical Diagnosis Interface (Fixed Version)"""
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import backend


class ModernDoctorHouseApp:
    """Modern medical-themed diagnosis application with professional UI - All issues fixed."""

    def __init__(self, my_root: tk.Tk) -> None:
        self.root = my_root
        self.root.title("Doctor House - AI Medical Diagnosis System")
        self.root.geometry("1200x800")
        self.widgets = {}

        # Color Palette - Medical Professional Theme (centralized)
        self.colors = {
            'primary': '#2C3E50',
            'secondary': '#3498DB',
            'accent': '#E74C3C',
            'success': '#27AE60',
            'warning': '#F39C12',
            'bg_main': '#ECF0F1',
            'bg_card': '#FFFFFF',
            'text_dark': '#2C3E50',
            'text_light': '#7F8C8D',
            'border': '#BDC3C7',
            'hover': '#3498DB',
            'shadow': '#95A5A6'
        }

        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", self.toggle_fullscreen)
        self.root.bind("<F1>", self.show_help)
        self.root.bind('<Configure>', self.on_window_configure)
        self.root.config(bg=self.colors['bg_main'])

        self.setup_styles()
        self.create_header()
        self.create_main_content()
        self.create_footer()

    def setup_styles(self) -> None:
        """Configure modern ttk styles with proper state handling"""
        style = ttk.Style(self.root)
        style.theme_use('clam')

        # Frame styles
        style.configure('Main.TFrame', background=self.colors['bg_main'])
        style.configure('Card.TFrame', background=self.colors['bg_card'], relief='flat')
        style.configure('Header.TFrame', background=self.colors['primary'])

        # Label styles
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

        # Button styles with proper disabled state
        style.configure('Primary.TButton',
                        background=self.colors['secondary'],
                        foreground='white',
                        borderwidth=0,
                        font=('Segoe UI', 11, 'bold'),
                        padding=(20, 12))

        style.map('Primary.TButton',
                  background=[('active', '#2980B9'), ('pressed', '#21618C'),
                              ('disabled', '#BDC3C7')],
                  foreground=[('disabled', '#7F8C8D')],
                  relief=[('pressed', 'flat')])

        style.configure('Danger.TButton',
                        background=self.colors['accent'],
                        foreground='white',
                        borderwidth=0,
                        font=('Segoe UI', 11, 'bold'),
                        padding=(20, 12))

        style.map('Danger.TButton',
                  background=[('active', '#C0392B'), ('disabled', '#BDC3C7')],
                  foreground=[('disabled', '#7F8C8D')],
                  relief=[('pressed', 'flat')])

        style.configure('Secondary.TButton',
                        background='white',
                        foreground=self.colors['text_dark'],
                        borderwidth=1,
                        font=('Segoe UI', 10),
                        padding=(15, 8))

        style.map('Secondary.TButton',
                  background=[('active', self.colors['bg_main']), ('disabled', '#ECF0F1')],
                  foreground=[('disabled', '#BDC3C7')],
                  bordercolor=[('active', self.colors['secondary'])])

    def create_header(self) -> None:
        """Create professional header with branding"""
        header_frame = ttk.Frame(self.root, style='Header.TFrame', height=120)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        header_frame.pack_propagate(False)

        header_content = ttk.Frame(header_frame, style='Header.TFrame')
        header_content.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)

        # Logo section
        logo_frame = ttk.Frame(header_content, style='Header.TFrame')
        logo_frame.pack(side=tk.LEFT)

        # Medical cross icon (replaced emoji with text symbol for consistency)
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
                             text="AI-Powered Medical Symptom Analysis | 133 Symptoms • 41 Diseases",
                             style='Subtitle.TLabel')
        subtitle.pack(anchor='w')

        # Action buttons (top right)
        button_frame = ttk.Frame(header_content, style='Header.TFrame')
        button_frame.pack(side=tk.RIGHT)

        help_btn = ttk.Button(button_frame,
                              text="? Help (F1)",
                              style='Secondary.TButton',
                              command=self.show_help)
        help_btn.pack(side=tk.LEFT, padx=5)

        about_btn = ttk.Button(button_frame,
                               text="ℹ About",
                               style='Secondary.TButton',
                               command=self.show_about)
        about_btn.pack(side=tk.LEFT, padx=5)

    def create_main_content(self) -> None:
        """Create main content area with modern card layout"""
        main_frame = ttk.Frame(self.root, style='Main.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=30)

        main_frame.columnconfigure(0, weight=1, minsize=400)
        main_frame.columnconfigure(1, weight=1, minsize=400)
        main_frame.rowconfigure(0, weight=1)

        self.create_symptom_card(main_frame)
        self.create_selection_card(main_frame)

    def create_symptom_card(self, parent: ttk.Frame) -> None:
        """Create left card for symptom search with improved shadow"""
        card_container = ttk.Frame(parent, style='Main.TFrame')
        card_container.grid(row=0, column=0, sticky='nsew', padx=(0, 15))

        # Improved shadow using canvas instead of frame
        shadow_canvas = tk.Canvas(card_container, bg=self.colors['bg_main'],
                                  highlightthickness=0, bd=0)
        shadow_canvas.place(x=0, y=0, relwidth=1, relheight=1)

        # Main card with slight elevation
        card = tk.Frame(card_container, bg=self.colors['bg_card'],
                        highlightbackground=self.colors['border'],
                        highlightthickness=1)
        card.place(x=0, y=0, relwidth=0.98, relheight=0.98)

        # Card header
        header = tk.Frame(card, bg=self.colors['bg_card'])
        header.pack(fill=tk.X, padx=30, pady=(30, 10))

        # Replaced emoji with descriptive text for cross-platform compatibility
        card_title = tk.Label(header,
                              text="🔍 Search Symptoms",
                              bg=self.colors['bg_card'],
                              fg=self.colors['text_dark'],
                              font=('Segoe UI', 14, 'bold'))
        card_title.pack(anchor='w')

        hint = tk.Label(header,
                        text="Type to search from 133 medical symptoms",
                        bg=self.colors['bg_card'],
                        fg=self.colors['text_light'],
                        font=('Segoe UI', 9, 'italic'))
        hint.pack(anchor='w', pady=(5, 0))

        # Search input container
        input_container = tk.Frame(card, bg=self.colors['bg_card'])
        input_container.pack(fill=tk.X, padx=30, pady=15)

        # Custom styled entry with focus feedback
        self.widgets["entry_frame"] = tk.Frame(input_container,
                                               bg=self.colors['bg_main'],
                                               highlightbackground=self.colors['border'],
                                               highlightthickness=2,
                                               highlightcolor=self.colors['secondary'])
        self.widgets["entry_frame"].pack(fill=tk.X)

        # Search icon (text-based for consistency)
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
        self.widgets["entry"].bind("<FocusIn>", self.on_entry_focus)
        self.widgets["entry"].bind("<FocusOut>", self.on_entry_unfocus)
        self.widgets["entry"].bind("<Down>", self.focus_dropdown)
        self.widgets["entry"].bind("<Return>", self.select_first_dropdown_item)

        # Info section
        info_frame = tk.Frame(card, bg=self.colors['bg_card'])
        info_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

        # Statistics cards
        stats_container = tk.Frame(info_frame, bg=self.colors['bg_card'])
        stats_container.pack(fill=tk.X, pady=10)

        self.create_stat_box(stats_container, "133", "Total Symptoms", 0)
        self.create_stat_box(stats_container, "41", "Diseases", 1)
        self.create_stat_box(stats_container, "AI", "Powered", 2)

        # Instructions
        instructions_frame = tk.Frame(info_frame, bg=self.colors['bg_card'])
        instructions_frame.pack(fill=tk.BOTH, expand=True, pady=20)

        instructions_title = tk.Label(instructions_frame,
                                      text="How to Use:",
                                      bg=self.colors['bg_card'],
                                      fg=self.colors['text_dark'],
                                      font=('Segoe UI', 12, 'bold'))
        instructions_title.pack(anchor='w', pady=(0, 10))

        instructions = [
            "1. Type symptom keywords in the search box",
            "2. Click symptoms from dropdown to select them",
            "3. Use Delete/Backspace to remove symptoms",
            "4. Click 'Analyze Symptoms' for diagnosis",
            "",
            "Keyboard shortcuts: F1=Help, ESC=Fullscreen"
        ]

        for instruction in instructions:
            label = tk.Label(instructions_frame,
                             text=instruction,
                             bg=self.colors['bg_card'],
                             fg=self.colors['text_light'],
                             font=('Segoe UI', 10),
                             anchor='w',
                             justify='left')
            label.pack(anchor='w', pady=2)

        # Dropdown (initially hidden) - improved positioning
        self.widgets["dropdown_frame"] = tk.Frame(self.root,
                                                  bg='white',
                                                  relief=tk.SOLID,
                                                  bd=1,
                                                  highlightbackground=self.colors['border'],
                                                  highlightthickness=0)

        self.widgets["listbox"] = tk.Listbox(self.widgets["dropdown_frame"],
                                             height=8,
                                             bg='white',
                                             fg=self.colors['text_dark'],
                                             selectbackground=self.colors['secondary'],
                                             selectforeground='white',
                                             font=('Segoe UI', 10),
                                             bd=0,
                                             highlightthickness=0,
                                             activestyle='dotbox')
        self.widgets["listbox"].pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.widgets["listbox"].bind("<ButtonRelease-1>", self.select_option)
        self.widgets["listbox"].bind("<Return>", self.select_option)
        self.widgets["listbox"].bind("<Escape>", lambda e: self.hide_dropdown(e))

    def create_selection_card(self, parent: ttk.Frame) -> None:
        """Create right card for selected symptoms"""
        card_container = ttk.Frame(parent, style='Main.TFrame')
        card_container.grid(row=0, column=1, sticky='nsew', padx=(15, 0))

        # Improved shadow
        shadow_canvas = tk.Canvas(card_container, bg=self.colors['bg_main'],
                                  highlightthickness=0, bd=0)
        shadow_canvas.place(x=0, y=0, relwidth=1, relheight=1)

        # Main card
        card = tk.Frame(card_container, bg=self.colors['bg_card'],
                        highlightbackground=self.colors['border'],
                        highlightthickness=1)
        card.place(x=0, y=0, relwidth=0.98, relheight=0.98)

        # Card header
        header = tk.Frame(card, bg=self.colors['bg_card'])
        header.pack(fill=tk.X, padx=30, pady=(30, 10))

        card_title = tk.Label(header,
                              text="✓ Selected Symptoms",
                              bg=self.colors['bg_card'],
                              fg=self.colors['text_dark'],
                              font=('Segoe UI', 14, 'bold'))
        card_title.pack(anchor='w')

        # Symptom count
        self.widgets["count_label"] = tk.Label(header,
                                               text="0 symptoms selected",
                                               bg=self.colors['bg_card'],
                                               fg=self.colors['text_light'],
                                               font=('Segoe UI', 9))
        self.widgets["count_label"].pack(anchor='w', pady=(5, 0))

        # Selected symptoms list with modern styling
        list_container = tk.Frame(card, bg=self.colors['bg_card'])
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
                                             highlightthickness=1,
                                             highlightbackground=self.colors['border'],
                                             selectbackground=self.colors['secondary'],
                                             selectforeground='white',
                                             yscrollcommand=scrollbar.set,
                                             activestyle='dotbox')
        self.widgets["lst_box"].pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.widgets["lst_box"].bind("<Delete>", self.remove_selected_symptom)
        self.widgets["lst_box"].bind("<BackSpace>", self.remove_selected_symptom)
        scrollbar.config(command=self.widgets["lst_box"].yview)

        # Action buttons
        button_frame = tk.Frame(card, bg=self.colors['bg_card'])
        button_frame.pack(fill=tk.X, padx=30, pady=(10, 30))

        self.widgets["btn_remove"] = ttk.Button(button_frame,
                                                text="🗑 Remove Selected",
                                                style='Secondary.TButton',
                                                command=self.remove_selected_symptom)
        self.widgets["btn_remove"].pack(fill=tk.X, pady=(0, 8))

        self.widgets["btn_clear"] = ttk.Button(button_frame,
                                               text="✕ Clear All",
                                               style='Secondary.TButton',
                                               command=self.clear_lst_box)
        self.widgets["btn_clear"].pack(fill=tk.X, pady=(0, 8))

        self.widgets["btn_submit"] = ttk.Button(button_frame,
                                                text="🔬 Analyze Symptoms",
                                                style='Primary.TButton',
                                                command=self.check_diagnosis)
        self.widgets["btn_submit"].pack(fill=tk.X)

        # Error/Success label
        self.widgets["label_error"] = tk.Label(button_frame,
                                               text="",
                                               bg=self.colors['bg_card'],
                                               fg=self.colors['accent'],
                                               font=('Segoe UI', 10, 'bold'),
                                               wraplength=350)
        self.widgets["label_error"].pack(pady=(10, 0))

    def create_stat_box(self, parent: tk.Frame, value: str, label: str, column: int) -> None:
        """Create a statistics display box"""
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
        """Create footer with disclaimer - improved visibility"""
        footer = tk.Frame(self.root, bg=self.colors['primary'], height=60)
        footer.pack(fill=tk.X, side=tk.BOTTOM)
        footer.pack_propagate(False)

        disclaimer = tk.Label(footer,
                              text="⚠ IMPORTANT DISCLAIMER: This tool is for educational purposes only. "
                                   "Always consult qualified healthcare professionals for medical advice and diagnosis.",
                              bg=self.colors['primary'],
                              fg='#ECF0F1',
                              font=('Segoe UI', 10, 'bold'),
                              wraplength=1100)
        disclaimer.pack(expand=True, pady=10)

    def on_window_configure(self, _event: tk.Event = None) -> None:
        """Reposition dropdown when window is resized or moved"""
        if self.widgets.get("dropdown_frame") and self.widgets["dropdown_frame"].winfo_ismapped():
            self.position_dropdown()

    def position_dropdown(self) -> None:
        """Calculate and set dropdown position relative to entry - fixed for resize"""
        if not self.widgets.get("entry_frame") or not self.widgets["entry_frame"].winfo_viewable():
            return

        try:
            x_size = self.widgets["entry_frame"].winfo_rootx() - self.root.winfo_rootx()
            y_size = (self.widgets["entry_frame"].winfo_rooty() - self.root.winfo_rooty() +
                      self.widgets["entry_frame"].winfo_height())
            width = self.widgets["entry_frame"].winfo_width()
            self.widgets["dropdown_frame"].place(x=x_size, y=y_size, width=width)
        except tk.TclError:
            # Widget not ready, skip positioning
            pass

    def on_entry_focus(self, _event: tk.Event = None) -> None:
        """Visual feedback when entry gets focus"""
        self.widgets["entry_frame"].config(highlightcolor=self.colors['secondary'],
                                           highlightthickness=2)
        self.update_list()

    def on_entry_unfocus(self, _event: tk.Event = None) -> None:
        """Visual feedback when entry loses focus"""
        self.widgets["entry_frame"].config(highlightcolor=self.colors['border'],
                                           highlightthickness=2)

    def focus_dropdown(self, _event: tk.Event = None) -> None:
        """Move focus to dropdown for keyboard navigation"""
        if self.widgets["listbox"].size() > 0:
            self.widgets["listbox"].focus_set()
            self.widgets["listbox"].selection_clear(0, tk.END)
            self.widgets["listbox"].selection_set(0)
            self.widgets["listbox"].activate(0)

    def select_first_dropdown_item(self, _event: tk.Event = None) -> None:
        """Select first item in dropdown when Enter is pressed in entry"""
        if self.widgets["listbox"].size() > 0:
            self.widgets["listbox"].selection_clear(0, tk.END)
            self.widgets["listbox"].selection_set(0)
            self.select_option(None)

    def update_symptom_count(self) -> None:
        """Update the symptom count label"""
        count = self.widgets["lst_box"].size()
        text = f"{count} symptom{'s' if count != 1 else ''} selected"
        self.widgets["count_label"].config(text=text)

    def toggle_fullscreen(self, _event: tk.Event = None) -> None:
        """Toggle fullscreen mode"""
        is_fullscreen = self.root.attributes('-fullscreen')
        self.root.attributes('-fullscreen', not is_fullscreen)

    def update_list(self, _event: tk.Event = None) -> None:
        """Update dropdown list based on user input with dynamic positioning"""
        typed = self.widgets["entry"].get().lower()
        self.widgets["listbox"].delete(0, tk.END)

        if not typed:
            self.widgets["dropdown_frame"].place_forget()
            return

        filtered = [symptom for symptom in SYMPTOM_OPTIONS if typed in symptom.lower()]

        if filtered:
            for item in filtered:
                self.widgets["listbox"].insert(tk.END, item)
            self.position_dropdown()
        else:
            self.widgets["dropdown_frame"].place_forget()

    def select_option(self, _event: tk.Event) -> None:
        """Select symptom from dropdown - prevent duplicates"""
        if not self.widgets["listbox"].curselection():
            return

        selected = self.widgets["listbox"].get(self.widgets["listbox"].curselection())

        # Check for duplicates
        current_items = self.widgets["lst_box"].get(0, tk.END)
        if selected in current_items:
            self.show_error("⚠ Symptom already added!", 2000)
            self.widgets["entry"].delete(0, tk.END)
            self.widgets["dropdown_frame"].place_forget()
            return

        self.widgets["entry"].delete(0, tk.END)
        self.widgets["lst_box"].insert(tk.END, selected)
        self.update_symptom_count()
        self.widgets["dropdown_frame"].place_forget()
        self.widgets["entry"].focus_set()

    def hide_dropdown(self, event: tk.Event) -> None:
        """Hide dropdown when clicking outside"""
        if event.widget not in (self.widgets["entry"], self.widgets["listbox"],
                                self.widgets["entry_frame"]):
            self.widgets["dropdown_frame"].place_forget()

    def remove_selected_symptom(self, _event: tk.Event = None) -> None:
        """Remove the currently selected symptom from the list"""
        selection = self.widgets["lst_box"].curselection()
        if selection:
            self.widgets["lst_box"].delete(selection[0])
            self.update_symptom_count()

    def clear_lst_box(self) -> None:
        """Clear selected symptoms with confirmation"""
        if self.widgets["lst_box"].size() > 0:
            response = messagebox.askyesno("Confirm Clear",
                                           "Are you sure you want to clear all selected symptoms?")
            if response:
                self.widgets["lst_box"].delete(0, tk.END)
                self.update_symptom_count()

    def clear_lst_box_silent(self) -> None:
        """Clear the list box without confirmation (used after diagnosis)"""
        self.widgets["lst_box"].delete(0, tk.END)
        self.update_symptom_count()

    def show_error(self, message: str, duration: int = 3000) -> None:
        """Show error message for specified duration"""
        self.widgets["label_error"].config(text=message, fg=self.colors['accent'])
        self.root.after(duration, lambda: self.widgets["label_error"].config(text=""))

    def show_success(self, message: str, duration: int = 2000) -> None:
        """Show success message for specified duration"""
        self.widgets["label_error"].config(text=message, fg=self.colors['success'])
        self.root.after(duration, lambda: self.widgets["label_error"].config(text=""))

    def check_diagnosis(self) -> None:
        """Calculate potential diseases with proper error handling"""
        patient_symptoms = list(self.widgets["lst_box"].get(0, tk.END))

        if not patient_symptoms:
            self.show_error("⚠ Please select at least one symptom", 3000)
            return

        # Show loading state with visual feedback
        self.widgets["btn_submit"].config(text="⏳ Analyzing...", state='disabled')
        self.widgets["btn_clear"].config(state='disabled')
        self.widgets["btn_remove"].config(state='disabled')
        self.root.update()

        try:
            result = backend.calculate_potential_disease(DIAGNOSIS_GRAPH, patient_symptoms)

            if not result:
                self.show_error("Unable to determine diagnosis. Please try different symptoms.", 3000)
                return

            ModernDiagnosisWindow(self.root, result)
            self.clear_lst_box_silent()
            self.show_success("✓ Diagnosis completed successfully", 2000)

        except Exception as e:
            self.show_error(f"Error during diagnosis: {str(e)}", 3000)
        finally:
            # Restore button states
            self.widgets["btn_submit"].config(text="🔬 Analyze Symptoms", state='normal')
            self.widgets["btn_clear"].config(state='normal')
            self.widgets["btn_remove"].config(state='normal')

    def show_help(self, _event: tk.Event = None) -> None:
        """Show help dialog - accessible"""
        help_text = """Doctor House - AI Medical Diagnosis System

HOW TO USE:
1. Type symptom keywords in the search box
2. Click symptoms from dropdown to add them
3. Use Delete/Backspace to remove selected symptom
4. Click "Analyze Symptoms" for diagnosis

KEYBOARD SHORTCUTS:
• F1 - Show this help
• ESC - Toggle fullscreen
• Down Arrow - Navigate to dropdown
• Enter - Select first/highlighted symptom
• Delete/Backspace - Remove selected symptom

UNDERSTANDING RESULTS:
• Red (>40%): High probability
• Orange (25-40%): Medium probability
• Blue (<25%): Lower probability

IMPORTANT DISCLAIMER:
This tool is for educational purposes only.
Always consult qualified healthcare professionals 
for medical advice, diagnosis, and treatment.

Database: 133 symptoms • 41 diseases"""

        messagebox.showinfo("Help - Doctor House", help_text)

    def show_about(self) -> None:
        """Show about dialog - modal and properly centered"""
        about_window = tk.Toplevel(self.root)
        about_window.title("About Doctor House")
        about_window.geometry("500x450")
        about_window.config(bg='white')
        about_window.resizable(False, False)

        # Make modal
        about_window.transient(self.root)
        about_window.grab_set()

        # Center window
        about_window.update_idletasks()
        x = (about_window.winfo_screenwidth() // 2) - (500 // 2)
        y = (about_window.winfo_screenheight() // 2) - (450 // 2)
        about_window.geometry(f'500x450+{x}+{y}')

        content = tk.Frame(about_window, bg='white')
        content.pack(fill=tk.BOTH, expand=True, padx=40, pady=30)

        # Icon
        icon = tk.Label(content,
                        text="⚕",
                        bg='white',
                        fg=self.colors['primary'],
                        font=('Segoe UI', 48))
        icon.pack(pady=(0, 10))

        title = tk.Label(content,
                         text="Doctor House",
                         bg='white',
                         fg=self.colors['primary'],
                         font=('Segoe UI', 24, 'bold'))
        title.pack(pady=(0, 5))

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

Developed for educational purposes.
Always consult healthcare professionals
for medical advice and treatment.

© 2024-2025 Doctor House Project"""

        text_label = tk.Label(content,
                              text=about_text,
                              bg='white',
                              fg=self.colors['text_dark'],
                              font=('Segoe UI', 10),
                              justify='center')
        text_label.pack(pady=15)

        close_btn = tk.Button(content,
                              text="Close",
                              bg=self.colors['secondary'],
                              fg='white',
                              font=('Segoe UI', 11, 'bold'),
                              bd=0,
                              padx=30,
                              pady=10,
                              cursor='hand2',
                              command=about_window.destroy)
        close_btn.pack(pady=10)


class ModernDiagnosisWindow:
    """Modern diagnosis results window - All issues fixed"""

    def __init__(self, parent: tk.Tk, data: dict) -> None:
        """Create modern diagnosis window"""
        self.pop_up = tk.Toplevel(parent)
        self.pop_up.title("Doctor House - Diagnosis Results")
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
            'text_light': '#7F8C8D',
            'border': '#BDC3C7'
        }

        self.pop_up.attributes('-fullscreen', True)
        self.pop_up.bind("<Escape>", self.toggle_fullscreen)
        self.pop_up.bind("<F1>", self.show_help)
        self.pop_up.config(bg=self.colors['bg_main'])

        # Make modal
        self.pop_up.transient(parent)
        self.pop_up.grab_set()

        self.create_header()
        self.create_results_content(data)
        self.create_footer()

    def create_header(self) -> None:
        """Create results header"""
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

        # Help button
        help_btn = tk.Button(content,
                             text="? Help (F1)",
                             bg=self.colors['secondary'],
                             fg='white',
                             font=('Segoe UI', 10, 'bold'),
                             bd=0,
                             padx=15,
                             pady=8,
                             cursor='hand2',
                             command=self.show_help)
        help_btn.pack(side=tk.RIGHT, padx=(0, 10))

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
        """Create main results content"""
        main_frame = tk.Frame(self.pop_up, bg=self.colors['bg_main'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=30)

        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)

        self.create_chart_panel(main_frame, data)
        self.create_details_panel(main_frame, data)

    def create_chart_panel(self, parent: tk.Frame, data: dict) -> None:
        """Create chart visualization panel - improved with vertical bars"""
        card_container = tk.Frame(parent, bg=self.colors['bg_main'])
        card_container.grid(row=0, column=0, sticky='nsew', padx=(0, 15))

        # Simplified shadow
        card = tk.Frame(card_container, bg=self.colors['bg_card'],
                        highlightbackground=self.colors['border'],
                        highlightthickness=1)
        card.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)

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

        # Chart - using vertical bars for better readability
        chart_frame = tk.Frame(card, bg=self.colors['bg_card'])
        chart_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        fig = Figure(figsize=(6, 6), dpi=100, facecolor=self.colors['bg_card'])
        ax = fig.add_subplot(111)

        categories = list(data.keys())
        values = list(data.values())

        # Adaptive color gradient based on actual data distribution
        max_val = max(values)
        colors_list = []
        for val in values:
            if val >= max_val * 0.7:  # Top 70% of max
                colors_list.append(self.colors['accent'])
            elif val >= max_val * 0.4:  # 40-70% of max
                colors_list.append(self.colors['warning'])
            else:
                colors_list.append(self.colors['secondary'])

        bars = ax.bar(categories, values, color=colors_list, edgecolor='white', linewidth=2)

        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2., height,
                    f'{height:.1f}%',
                    ha='center', va='bottom',
                    fontsize=10, fontweight='bold',
                    color=self.colors['text_dark'])

        ax.set_ylabel('Probability (%)', fontsize=11, fontweight='bold', color=self.colors['text_dark'])
        ax.set_xlabel('Disease', fontsize=11, fontweight='bold', color=self.colors['text_dark'])
        ax.set_title('Likelihood Assessment', fontsize=13, fontweight='bold', pad=15,
                     color=self.colors['text_dark'])
        ax.set_ylim(0, min(110, max(values) * 1.15))

        # Rotate labels for readability with dark color
        ax.tick_params(axis='x', rotation=20, labelsize=9, colors=self.colors['text_dark'],
                       labelcolor=self.colors['text_dark'])
        ax.tick_params(axis='y', labelsize=9, colors=self.colors['text_dark'],
                       labelcolor=self.colors['text_dark'])

        # Clean styling
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color(self.colors['text_dark'])
        ax.spines['bottom'].set_color(self.colors['text_dark'])
        ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.7, color=self.colors['text_dark'])
        ax.set_axisbelow(True)

        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def create_details_panel(self, parent: tk.Frame, data: dict) -> None:
        """Create disease details panel"""
        card_container = tk.Frame(parent, bg=self.colors['bg_main'])
        card_container.grid(row=0, column=1, sticky='nsew', padx=(15, 0))

        # Simplified shadow
        card = tk.Frame(card_container, bg=self.colors['bg_card'],
                        highlightbackground=self.colors['border'],
                        highlightthickness=1)
        card.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)

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

        # Disease buttons with adaptive color coding
        button_container = tk.Frame(card, bg=self.colors['bg_card'])
        button_container.pack(fill=tk.X, padx=30, pady=15)

        max_prob = max(data.values())
        for i, (disease, prob) in enumerate(data.items()):
            # Adaptive color based on relative probability
            if prob >= max_prob * 0.7:
                bg_color = self.colors['accent']
            elif prob >= max_prob * 0.4:
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
                            activebackground=self.colors['success'],
                            activeforeground='white',
                            command=lambda d=disease: self.show_info(d))
            btn.pack(fill=tk.X, pady=4)

        # Info display area
        info_container = tk.Frame(card, bg=self.colors['bg_main'])
        info_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=(10, 30))

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

        # Initial helpful message
        self.elements["info_text"].insert('1.0',
                                          "👆 Click on a disease button above to view:\n\n"
                                          "  • Detailed medical description\n"
                                          "  • Recommended precautions\n"
                                          "  • Medical advice\n\n"
                                          "Color coding indicates probability:\n"
                                          "  🔴 Red = Highest probability\n"
                                          "  🟠 Orange = Medium probability\n"
                                          "  🔵 Blue = Lower probability\n\n"
                                          "Remember: This is for educational purposes only.")
        self.elements["info_text"].config(state='disabled')

    def create_footer(self) -> None:
        """Create footer with enhanced disclaimer"""
        footer = tk.Frame(self.pop_up, bg=self.colors['primary'], height=60)
        footer.pack(fill=tk.X)
        footer.pack_propagate(False)

        text = tk.Label(footer,
                        text="⚠ CRITICAL DISCLAIMER: These results are probabilistic estimates based on symptom matching. "
                             "This is NOT a medical diagnosis. Always consult qualified healthcare professionals for "
                             "accurate diagnosis and treatment.",
                        bg=self.colors['primary'],
                        fg='#ECF0F1',
                        font=('Segoe UI', 10, 'bold'),
                        wraplength=1100)
        text.pack(expand=True, pady=10)

    def show_info(self, selected: str) -> None:
        """Display disease information with improved formatting"""
        self.elements["info_text"].config(state='normal')
        self.elements["info_text"].delete('1.0', tk.END)

        # Disease name
        self.elements["info_text"].insert(tk.END, f"{selected}\n", 'title')
        self.elements["info_text"].insert(tk.END, "═" * 60 + "\n\n", 'separator')

        # Description
        self.elements["info_text"].insert(tk.END, "📋 MEDICAL DESCRIPTION\n", 'section')
        self.elements["info_text"].insert(tk.END, f"{DISEASE_DICT[selected].description}\n\n", 'content')

        # Precautions
        self.elements["info_text"].insert(tk.END, "⚕ RECOMMENDED PRECAUTIONS\n", 'section')
        for i, precaution in enumerate(DISEASE_DICT[selected].advice, 1):
            self.elements["info_text"].insert(tk.END, f"  {i}. {precaution}\n", 'content')

        # Disclaimer
        self.elements["info_text"].insert(tk.END, "\n" + "─" * 60 + "\n", 'separator')
        self.elements["info_text"].insert(tk.END,
                                          "⚠ IMPORTANT: This information is for educational purposes only. "
                                          "These precautions are general recommendations. Always consult "
                                          "qualified healthcare professionals for personalized medical advice "
                                          "and treatment plans.\n",
                                          'disclaimer')

        # Configure tags
        self.elements["info_text"].tag_config('title',
                                              font=('Segoe UI', 16, 'bold'),
                                              foreground=self.colors['primary'])
        self.elements["info_text"].tag_config('separator',
                                              foreground=self.colors['border'])
        self.elements["info_text"].tag_config('section',
                                              font=('Segoe UI', 12, 'bold'),
                                              foreground=self.colors['secondary'],
                                              spacing1=10)
        self.elements["info_text"].tag_config('content',
                                              font=('Segoe UI', 11),
                                              spacing1=5,
                                              lmargin1=20,
                                              lmargin2=35)
        self.elements["info_text"].tag_config('disclaimer',
                                              font=('Segoe UI', 10, 'bold'),
                                              foreground=self.colors['accent'],
                                              spacing1=5)

        self.elements["info_text"].config(state='disabled')

    def toggle_fullscreen(self, _event: tk.Event = None) -> None:
        """Toggle fullscreen"""
        is_fullscreen = self.pop_up.attributes('-fullscreen')
        self.pop_up.attributes('-fullscreen', not is_fullscreen)

    def show_help(self, _event: tk.Event = None) -> None:
        """Show help dialog - accessible"""
        help_text = """Diagnosis Results Window

UNDERSTANDING YOUR RESULTS:
The chart shows the probability of each disease
based on symptom matching in our database.

COLOR CODING (Adaptive):
• Red buttons: Highest probability
• Orange buttons: Medium probability
• Blue buttons: Lower probability

Percentages are relative to your specific
symptom combination.

HOW TO USE:
1. Review the probability chart
2. Click disease buttons to view details
3. Read descriptions and precautions
4. Note recommendations carefully

IMPORTANT DISCLAIMER:
These are probabilistic estimates based on
symptom pattern matching, NOT actual medical
diagnoses. The system analyzes 133 symptoms
across 41 diseases using graph algorithms.

ALWAYS consult qualified healthcare
professionals for:
• Accurate diagnosis
• Treatment plans
• Medical advice
• Emergency care

This tool is for educational purposes only.

Press ESC to toggle fullscreen mode."""

        messagebox.showinfo("Help - Diagnosis Results", help_text)


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
