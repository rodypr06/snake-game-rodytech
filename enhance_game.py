"""
CrewAI Enhancement Crew for Snake Game
Improves gameplay mechanics and visual presentation
"""

from crewai import Agent, Task, Crew, Process
import os


def create_game_enhancement_crew():
    """Create a crew to enhance the Snake game with progressive speed and larger size"""

    # Agent 1: Game Balance Designer
    game_designer = Agent(
        role='Game Balance & Mechanics Designer',
        goal='Design progressive difficulty system with speed scaling based on score',
        backstory="""You are an expert game designer specializing in classic arcade game balance.
        You understand how to create engaging difficulty curves that start easy and progressively
        challenge players. You know the perfect speed scaling formulas for Snake games.""",
        verbose=True,
        allow_delegation=False
    )

    # Agent 2: Frontend Developer
    developer = Agent(
        role='Frontend Game Developer',
        goal='Implement progressive speed mechanics and increase canvas size while maintaining visual quality',
        backstory="""You are a skilled JavaScript developer with expertise in HTML5 Canvas games.
        You can modify game loops, implement dynamic speed systems, and scale game elements
        while preserving visual quality and gameplay feel.""",
        verbose=True,
        allow_delegation=False
    )

    # Agent 3: Playtester
    tester = Agent(
        role='Gameplay Quality Tester',
        goal='Validate that speed progression feels natural and canvas size is optimal',
        backstory="""You are an experienced game tester who evaluates gameplay feel and balance.
        You can analyze code to verify mechanics work correctly and suggest improvements
        for better player experience.""",
        verbose=True,
        allow_delegation=False
    )

    # Task 1: Design the speed progression system
    design_task = Task(
        description="""Design a progressive speed system for the Snake game:

        Requirements:
        1. Start at a comfortable slow speed (150ms per frame initially)
        2. Increase speed gradually as the snake eats apples
        3. Speed should increase by 3-5ms per apple eaten
        4. Minimum speed cap at 60ms (maximum speed)
        5. Speed should make the game progressively challenging but fair

        Also specify:
        - Larger canvas size (upgrade from 400x400 to 600x600 or 800x800)
        - Maintain grid size at 20px for better control
        - Calculate new tile count based on canvas size

        Provide exact parameters for implementation.
        """,
        expected_output="Detailed speed progression formula and canvas size specifications",
        agent=game_designer
    )

    # Task 2: Implement the enhancements
    develop_task = Task(
        description="""Modify static/game.html to implement progressive speed and larger canvas:

        Changes needed:
        1. Change initial game speed from 100ms to 150ms
        2. Add speed tracking variable that starts at 150
        3. Decrease speed by 4ms each time food is eaten (faster = lower interval)
        4. Set minimum speed limit at 60ms
        5. Update setInterval to use dynamic speed variable
        6. Increase canvas width and height to 600x600
        7. Recalculate tileCount based on new canvas size
        8. Ensure all visual elements scale properly
        9. Update any hardcoded positions if needed

        Preserve all the realistic graphics improvements (shadows, gradients, particles, etc.)

        Read the current game.html file, make the necessary modifications, and write the updated version.
        """,
        expected_output="Updated game.html file with progressive speed and larger canvas",
        agent=developer,
        context=[design_task]
    )

    # Task 3: Validate the changes
    test_task = Task(
        description="""Review the enhanced game implementation:

        Verify:
        1. Initial speed is comfortable for new players (150ms)
        2. Speed increases correctly after each apple (decreases interval by 4ms)
        3. Speed caps at 60ms to prevent unplayable difficulty
        4. Canvas is larger (600x600) with proper tile count
        5. All visual elements (snake, apple, grid) scale correctly
        6. Particle effects still work properly
        7. Game remains playable and balanced

        Provide a brief validation report.
        """,
        expected_output="Validation report confirming enhancements work correctly",
        agent=tester,
        context=[design_task, develop_task]
    )

    # Create the crew
    crew = Crew(
        agents=[game_designer, developer, tester],
        tasks=[design_task, develop_task, test_task],
        process=Process.sequential,
        verbose=True
    )

    return crew


def main():
    """Run the CrewAI enhancement workflow"""
    print("🎮 Starting CrewAI Snake Game Enhancement Crew...\n")
    print("=" * 60)
    print("Enhancements:")
    print("  1. Progressive speed system (slow → fast)")
    print("  2. Larger canvas (600x600)")
    print("  3. Maintain all realistic graphics")
    print("=" * 60)
    print()

    # Create and run the crew
    crew = create_game_enhancement_crew()
    result = crew.kickoff()

    print("\n" + "=" * 60)
    print("🎉 CrewAI Enhancement Complete!")
    print("=" * 60)
    print("\nFinal Result:")
    print(result)
    print("\n✅ Game enhanced: static/game.html")
    print("🔄 Restart server to see changes")


if __name__ == "__main__":
    main()
