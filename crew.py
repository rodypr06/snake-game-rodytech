"""
CrewAI Multi-Agent System for Snake Game Development
Demonstrates agent collaboration: Designer → Developer → Tester
"""

from crewai import Agent, Task, Crew, Process
import os


def create_game_development_crew():
    """Create a crew of agents to collaboratively build a Snake game"""

    # Agent 1: Game Designer
    designer = Agent(
        role='Game Designer & Architect',
        goal='Design a simple, fun web-based Snake game with clear specifications',
        backstory="""You are an experienced game designer with expertise in classic arcade games.
        You excel at creating engaging, simple game mechanics and defining clear technical requirements.
        You understand web technologies and can specify games that are easy to implement.""",
        verbose=True,
        allow_delegation=False
    )

    # Agent 2: Full-Stack Developer
    developer = Agent(
        role='Full-Stack Web Developer',
        goal='Implement a web-based Snake game using HTML5, CSS3, and JavaScript',
        backstory="""You are a skilled full-stack developer specializing in web game development.
        You can create engaging games using vanilla JavaScript and HTML5 Canvas.
        You write clean, well-structured code with proper separation of concerns.""",
        verbose=True,
        allow_delegation=False
    )

    # Agent 3: QA Tester
    tester = Agent(
        role='Quality Assurance Engineer',
        goal='Test the Snake game thoroughly and provide detailed feedback',
        backstory="""You are a meticulous QA engineer with expertise in game testing.
        You can identify bugs, edge cases, and usability issues by analyzing code.
        You provide constructive feedback to improve game quality.""",
        verbose=True,
        allow_delegation=False
    )

    # Task 1: Design the game
    design_task = Task(
        description="""Design a simple web-based Snake game with the following requirements:
        - Classic Snake gameplay mechanics
        - Web-based using HTML5 Canvas
        - Simple controls (arrow keys)
        - Score tracking
        - Game over and restart functionality

        Provide a clear design specification including:
        1. Game mechanics (movement, collision, food, scoring)
        2. Technical architecture (file structure, key functions)
        3. UI/UX layout (canvas size, colors, styling)
        4. Control scheme
        """,
        expected_output="A detailed game design document with specifications for implementation",
        agent=designer
    )

    # Task 2: Implement the game
    develop_task = Task(
        description="""Based on the design specifications, create a complete web-based Snake game.

        Create a single HTML file that includes:
        1. HTML5 Canvas for game rendering
        2. CSS for styling with a modern, clean look
        3. JavaScript for game logic including:
           - Snake movement and growth
           - Food generation
           - Collision detection (walls and self)
           - Score tracking
           - Game over and restart
           - Keyboard controls

        The game should be:
        - Self-contained in one HTML file
        - Playable immediately when opened in a browser
        - Visually appealing with smooth animations
        - Responsive and bug-free

        Write the complete game code to static/game.html
        """,
        expected_output="Complete, working Snake game in static/game.html file",
        agent=developer,
        context=[design_task]
    )

    # Task 3: Test the game
    test_task = Task(
        description="""Review and test the Snake game implementation.

        Analyze the code and provide a test report covering:
        1. Code quality and structure
        2. Game mechanics verification (does it match the design?)
        3. Potential bugs or edge cases
        4. User experience assessment
        5. Suggestions for improvements

        Your report should be constructive and specific.
        """,
        expected_output="Comprehensive test report with findings and recommendations",
        agent=tester,
        context=[design_task, develop_task]
    )

    # Create the crew
    crew = Crew(
        agents=[designer, developer, tester],
        tasks=[design_task, develop_task, test_task],
        process=Process.sequential,
        verbose=True
    )

    return crew


def main():
    """Run the CrewAI game development workflow"""
    print("🎮 Starting CrewAI Snake Game Development Crew...\n")
    print("=" * 60)
    print("This crew will collaboratively build a Snake game:")
    print("  1. Designer: Creates game specifications")
    print("  2. Developer: Implements the game")
    print("  3. Tester: Validates and provides feedback")
    print("=" * 60)
    print()

    # Create output directory
    os.makedirs('static', exist_ok=True)

    # Create and run the crew
    crew = create_game_development_crew()
    result = crew.kickoff()

    print("\n" + "=" * 60)
    print("🎉 CrewAI Development Complete!")
    print("=" * 60)
    print("\nFinal Result:")
    print(result)
    print("\n✅ Game file created: static/game.html")
    print("🚀 Run 'python server.py' to start the web server on port 2025")


if __name__ == "__main__":
    main()
