import pygame
import random
active = True
score = 0

def main():
    pygame.init()

    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Påskequiz")
        
 
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    FONT = pygame.font.Font(None, 36)
    

    questions = [
        {"question": "Hva feirer vi i påsken?", "options": ["Jul", "Jesus' oppstandelse", "Halloween"], "answer": 1, "image": "easter.jpg"},
        {"question": "Hva heter den tradisjonelle norske påskedesserten?", "options": ["Riskrem", "Karamellpudding", "Appelsin"], "answer": 2, "image": "orange.jpg"}
    ]
    
    running = True
    while running:
        screen.fill(WHITE)
        question = random.choice(questions)
        text = FONT.render(question["question"], True, BLACK)
        screen.blit(text, (50, 50))
        
        pygame.display.update()
        pygame.time.wait(3000)
        running = False
    
    pygame.quit()

if __name__ == "__main__":
    main()
