# Project: Space Invador EX [TBD]

## The Big Idea
### Gameplay
Players control a spaceship that can move horizontally and shoot laser beams. A matrix of enemies approaches from the top of the screen. The player must use the laser to destroy all the enemies to win the game. In each time unit in the game, the enemies move forward. If any enemy crosses the bottom line, the game is over. (This is the original Space Invador game)

The game consists of multiple stages, including battles, events, gifts, shops, and boss fights. Across different stages, the player can develop their abilities and battle stronger aliens. In this prototype each of these stages will be created and will be a five part level for the entire playthrough. (This is the RPG system that I want to incorporate with)

### Goal
**Core Challenge**:
The main challenge is to eliminate all enemies before they reach the bottom line.

**Core Achievement**:
The key achievement involves skillfully maneuvering the spaceship to hit enemies while dodging their shots. The game introduces a rising difficulty curve with less reaction time and more agile enemies. Meanwhile, the player grows increasingly powerful with various abilities, allowing for the creation of unique builds.

### Player Inputs:

**Moving:**

- The player controls a spaceship moving along a horizontal line.
- The spaceship is confined to the width of this line and cannot move beyond it.
- Movement is at a constant pace, without acceleration or inertia.

**Shooting:**

- The spaceship fires a laser beam that moves at a constant pace when the player inputs the command.
- The projectile has no acceleration or inertia.
- The direction of the laser beam is always exactly aligned with the player's direction, perpendicular to the bottom line.
  
### Other Logics
**Mechanics:**
- 3Cs (Character, Control, Camera)
- Combat HUD (Health bar system, enemy health bar, ability slots)

**Dynamics:**
- Currency system
- Combat system (the flow of resources)
- Difficulty curve
- Reward Settlement System
- The rogue-like RPG system

**Aesthetics:**
- Pixel art done in Python, no external resources

**NPCs:**
- Boss design
- Three different enemy designs

Although it seems extensive, I am aware of the scale of the prototype. Most systems mentioned here already exist in Space Invaders. The only new additions are the NPC designs (in the original Space Invaders, all NPCs behave the same) and the RPG system, which is limited to just a handful (<3) of abilities.

## Learning Objective
Learn to use Pygame as a package for simple prototype development. I aim to explore the strengths of using Python for simulating basic game logic and compare its advantages to those of Unity or Unreal Engine for building prototypes. Additionally, I want to understand how Python handles visualization. Finally, I plan to create 8-bit music using the library, as I assume that, unlike game engines with asset management, all assets here are created by the program.

## Implementation Plan

1. Pygame: Pygame is the primary package I'll be using. It's great for 2D game development and prototyping, providing functionalities for graphics, sound, and input handling. I can also create pixel art and basic AIs using it
2. Pandas: Helpful for managing game data like currency systems, player stats, etc.
3. Pygame.mixer: It is a part of Pygame, which can be used for incorporating 8-bit music and sound effects.

There is a tutorial on Youtube on making a Space Invador game using Pygame. [Creating Space Invaders in Pygame/Python](https://youtu.be/o-6pADy5Mdg?si=NCwg8PInHN5cW3ey). I will follow the video and produce the basic Space Invador prototype and then add the rpg system on to that.

## Project Schedule

**Project Timeline:**

1. **Half Week:**
   - Game Design Document

2. **Half Week:**
   - Brainstorm RPG System
   - Write the Logic

3. **1 Week:**
   - Basic Space Invaders System
   - (Expected output, no need for feedback update loop)

4. **1 Week:**
   - New Combat System

5. **1 Week:**
   - RPG System Implementation

6. **2 Weeks:**
   - Game Testing
   - Updates and Iterations

## Collaboration Plan 
- No collaboration
- Will invite people to play test

## Risk and Limitation

The RPG system poses the greatest challenge in programming. It is designed to allow multiple abilities to interact and produce non-linear improvements. However, the logic behind these calculations can lead to bugs and requires a clear understanding of various trigger conditions.

## Additional Course Content
Object-oriented programming can be beneficial. Although I have some experience with class-based programming in C#, understanding the nuances of Python in this regard would still be valuable.