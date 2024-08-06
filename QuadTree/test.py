import pygame

from random import randint
from Quadtree import *
from Particle import Particle
from pygame.math import Vector2
from range import *

Width, Height = 1200, 800
screen = pygame.display.set_mode((Width, Height))

pygame.display.set_caption("Quadtree")
clock = pygame.time.Clock()
fps = 60

bg_image = pygame.image.load('map.png')
particles = []
RADIUS = 10

NODE_CAPACITY = 1

rangeRect = Rectangle(Vector2(100, 100), Vector2(100, 100))
rangeRect.color = (0, 0, 255)
rangeRect.lineThickness = 3

boundary = Rectangle(Vector2(0, 0), Vector2(Width, Height))

quadtree = QuadTree(NODE_CAPACITY, boundary)

#for i in range(150):
#    offset = 50
#    x = randint(offset, Width-offset)
#    y = randint(offset, Height-offset)
#    # col = (randint(0, 255), randint(0, 255),randint(0, 255))
#    col = (255, 255, 0)
#    particle = Particle(Vector2(x, y), RADIUS, col)
#    quadtree.insert(particle)
#    particles.append(particle)


# print(points)
moveParticle = False
particleCollision = False
showRange = True
run = True
while run:
    screen.blit(bg_image, (0, 0))
    pygame.display.set_caption("QuadTree Fps: " + str(int(clock.get_fps())))
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                showRange = not showRange
            if event.key == pygame.K_e:
                moveParticle = not moveParticle
                particleCollision = moveParticle
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            particle = Particle(Vector2(x, y), RADIUS, (255, 255, 0))
            particles.append(particle)
            quadtree.insert(particle)


    quadtree.Show(screen)

    for particle in particles:
        if moveParticle:
            particle.move()
        particle.draw(screen)

    rangeRect.position.x, rangeRect.position.y = pygame.mouse.get_pos()
    points = quadtree.queryRange(rangeRect)
    if showRange == True:
        for point in points:
            point.Highlight((0, 0, 255))
            point.draw(screen, RADIUS + 2)
        rangeRect.Draw(screen)
    pygame.display.flip()

pygame.quit()
