/* Personal Portfolio - console menu program (C) */
#include <stdio.h>

void about(void) {
    printf("\n--- ABOUT ME ---\n");
    printf("Name       : Your Name\n");
    printf("Course     : BCA, Semester III\n");
    printf("University : JECRC University\n");
    printf("Interest   : Programming and web development\n");
}

void skills(void) {
    printf("\n--- SKILLS ---\n");
    printf("1. C / C++\n2. Java\n3. Python\n4. HTML, CSS, JavaScript\n");
}

void projects(void) {
    printf("\n--- PROJECTS ---\n");
    printf("1. Profile Page (Python, dark/light mode)\n");
    printf("2. Quiz App (C++)\n");
    printf("3. Personal Portfolio (C)\n");
    printf("4. Mini Web App (Python)\n");
    printf("5. Weather App (Java, OpenWeatherMap)\n");
}

void contact(void) {
    printf("\n--- CONTACT ---\n");
    printf("Email  : yourname@example.com\n");
    printf("GitHub : github.com/your-username\n");
}

int main(void) {
    int choice;
    do {
        printf("\n===== PERSONAL PORTFOLIO =====\n");
        printf("1. About\n2. Skills\n3. Projects\n4. Contact\n5. Exit\n");
        printf("Enter choice: ");
        if (scanf("%d", &choice) != 1) {
            while (getchar() != '\n');
            choice = 0;
        }
        switch (choice) {
            case 1: about(); break;
            case 2: skills(); break;
            case 3: projects(); break;
            case 4: contact(); break;
            case 5: printf("Thank you for visiting!\n"); break;
            default: printf("Invalid choice, try again.\n");
        }
    } while (choice != 5);
    return 0;
}
