from controllers import ElectionController
from views import MainApplication
from storage import load_data, save_data

def main():
    controller = ElectionController()
    # Initialize candidates here or load from file
    controller.add_candidate('Landon')
    controller.add_candidate('Javier')
    controller.add_candidate('Marlin')

    load_data(controller)  # Load data if available

    app = MainApplication(controller)
    app.protocol("WM_DELETE_WINDOW", lambda: on_close(app, controller))  # Handle window close event
    app.mainloop()

def on_close(app: MainApplication, controller: ElectionController):
    save_data(controller)  # Save data on close
    app.destroy()

if __name__ == '__main__':
    main()
