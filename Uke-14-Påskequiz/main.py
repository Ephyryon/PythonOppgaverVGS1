import pygame

questions = [
    {"question": "Hvor (sted) er påsken fra?", "options": {"Nord-Europa", "Midt-Østen", "West-Europa", "Sentral-Europa"}, "answer": "Midt-Østen"},
    {"question": "Svaret var Midt-Østen", "options": {"Neste"}, "answer": ""},
    {"question": "Hvilke religion kommer påske fra?", "options": {"Kristendommen", "Romersk paganisme", "Jødedommen", "Hellenisk paganisme"}, "answer": "Kristendommen"},
    {"question": "Svaret var Kristendommen", "options": {"Neste"}, "answer": ""},
    {"question": "Hva feirer vi i påsken?", "options": {"Jul", "Jesus' oppstandelse", "Halloween"}, "answer": "Jesus' oppstandelse"},
    {"question": "Svaret var Jesus' oppstandelse", "options": {"Neste"}, "answer": ""},
    {"question": "Hva heter den tradisjonelle norske påskedesserten?", "options": {"Riskrem", "Karamellpudding", "Appelsin"}, "answer": "Appelsin"},
    {"question": "Svaret var Appelsin", "options": {"Neste"}, "answer": ""},
    {"question": "Hvilket dyr blir ofte koblet sammen med påsken?", "options": {"And", "Hare", "Lamb", "Rådyr"}, "answer": "Hare"},
    {"question": "Svaret var Hare", "options": {"Neste"}, "answer": ""},
    {"question": "Hvilket land forbindes med tradisjonen om påskeharen?", "options": {"Tyskland", "Frankrike", "Italia", "Norge"}, "answer": "Tyskland"},
    {"question": "Svaret var Tyskland", "options": {"Neste"}, "answer": ""},
    {"question": "Hva symboliserer påskeegget?", "options": {"Liv og oppstandelse", "Jesus' lidelse", "Judas' svik", "Disiplenes tro"}, "answer": "Liv og oppstandelse"},
    {"question": "Svaret var Liv og oppstandelse", "options": {"Neste"}, "answer": ""},
    {"question": "Hvor mange dager varer fasten før påske?", "options": {"25", "40", "50", "30"}, "answer": "40"},
    {"question": "Svaret var 40", "options": {"Neste"}, "answer": ""},
    {"question": "Hva er typisk norsk påskemat?", "options": {"Kylling", "Torsk", "Lam", "Kalkun"}, "answer": "Lam"},
    {"question": "Svaret var Lam", "options": {"Neste"}, "answer": ""},
    {"question": "Hvilken farge forbindes ofte med påsken i kristendommen?", "options": {"Grønn", "Rød", "Blå", "Lilla"}, "answer": "Lilla"},
    {"question": "Svaret var Lilla", "options": {"Neste"}, "answer": ""},
    {"question": "Hvilket land produserer mest påskesjokolade i verden?", "options": {"Tyskland", "Sveits", "Storbritannia", "USA"}, "answer": "Storbritannia"},
    {"question": "Svaret var Storbritannia", "options": {"Neste"}, "answer": ""},
    {"question": "Hva er 'Påskeøya' mest kjent for?", "options": {"Store steinstatuer", "Store påskefeiringer", "Vulkanutbrudd", "Fargerike hus"}, "answer": "Store steinstatuer"},
    {"question": "Svaret var Store steinstatuer", "options": {"Neste"}, "answer": ""},
    {"question": "Hva er 'påskelam' et symbol på i kristendommen?", "options": {"Guds vrede", "Jesu offerdød", "Påskens glede", "Jomfru Marias renhet"}, "answer": "Jesu offerdød"},
    {"question": "Svaret var Jesu offerdød", "options": {"Neste"}, "answer": ""},
    {"question": "Hvorfor kalles det 'Gul påske'?", "options": {"Fordi påskeliljer og kyllinger er gule", "Fordi kirken bruker gult under påskemessen", "Fordi solen alltid skinner i påsken", "Fordi Jesus hadde en gul kappe"}, "answer": "Fordi påskeliljer og kyllinger er gule"},
    {"question": "Svaret var Fordi påskeliljer og kyllinger er gule", "options": {"Neste"}, "answer": ""},
    {"question": "Hva heter fjellvettregel nummer 1, som mange forbinder med påsken?", "options": {"Ta alltid med ekstra klær", "Ikke gå alene på tur", "Planlegg turen og meld fra hvor du går", "Lytt til værmeldingen"}, "answer": "Planlegg turen og meld fra hvor du går"},
    {"question": "Svaret var Planlegg turen og meld fra hvor du går", "options": {"Neste"}, "answer": ""},
    {"question": "Gratulerer! Du gjorde ferdig quizen.", "options": {"Prøv igjen.", "Avslutt"}, "answer": ""}
]

score = 0

pygame.init()
WIDTH, HEIGHT = 800, 400
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
        x = (WIDTH - text_width) // 2.1
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
                    if ques < len(questions) - 1:
                        ques += 1
                        buttons = button_create(questions[ques]["options"])
                    else:
                        screen.blit(text2, ((WIDTH - text2.get_width()) // 2, 300))
    pygame.display.flip()
 
pygame.quit()