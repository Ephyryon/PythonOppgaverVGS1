import pygame

score = 0

questions = [
    {"question": "Hvor (sted) er påsken fra?", "options": {"Nord-Europa", "Midt-Østen", "West-Europa", "Sentral-Europa"}, "answer": "Midt-Østen"},
    {"question": "Hvilke religion kommer påske fra?", "options": {"Kristendommen", "Romersk paganisme", "Jødedommen", "Hellenisk paganisme"}, "answer": "Kristendommen"},
    {"question": "Hva feirer vi i påsken?", "options": {"Jul", "Jesus' oppstandelse", "Halloween"}, "answer": "Jesus' oppstandelse"},
    {"question": "Hva heter den tradisjonelle norske påskedesserten?", "options": {"Riskrem", "Karamellpudding", "Appelsin"}, "answer": "Appelsin"},
    {"question": "Gratulerer! Du gjorde ferdig quizen.", "options": {"Prøv igjen.", "Avslutt"}, "answer": ""}
]

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Påskequiz")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 180)
font = pygame.font.Font(None, 28)

ques = 0

def button_create(options):
    button_height = 50
    button_spacing = 10
    buttons = []
    for i, option in enumerate(options):
        text_width, text_height = font.size(option)
        button_width = text_width + 40
        x = 275 - text_width//2
        y = 90 + (i*(50+button_spacing))
        rect = pygame.Rect(x, y, button_width, button_height)
        buttons.append((rect, option, i))
    return buttons

buttons = button_create(questions[ques]["options"])
running = True
while running:
    screen.fill((30, 30, 30))
    
    text = font.render(questions[ques]["question"], True, WHITE)
    screen.blit(text, ((WIDTH - text.get_width()) // 2, 50))
    text2 = font.render(f"Du fikk en poengsum på: {score}", True, WHITE)
    if ques == len(questions)-1:
        screen.blit(text2, ((WIDTH - text2.get_width()) // 2, 300))

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    for rect, text, index in buttons:
        button_color = DARK_BLUE if rect.collidepoint(mouse_pos) else BLUE
        pygame.draw.rect(screen, button_color, rect, border_radius=10)


        text_surface = font.render(text, True, WHITE)
        text_x = rect.x + (rect.width - text_surface.get_width()) // 2
        text_y = rect.y + (rect.height - text_surface.get_height()) // 2
        screen.blit(text_surface, (text_x, text_y))    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for rect, text, index in buttons:
                if rect.collidepoint(mouse_pos):
                    answer = questions[ques]["answer"]
                    print(f"Button '{text}' clicked!")
                    if text == "Avslutt":
                        pygame.quit()
                    if text == "Prøv igjen.":
                        ques = -1
                        score = 0
                        buttons = button_create(questions[ques]["options"])
                    if text == answer:
                        score += 1
                    print(score)
                    if ques < len(questions) - 1:
                        ques += 1
                        buttons = button_create(questions[ques]["options"])
                    else:
                        screen.blit(text2, ((WIDTH - text2.get_width()) // 2, 300))
    pygame.display.flip()
 
pygame.quit()