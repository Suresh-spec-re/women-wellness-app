<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Women's Empowerment and Safety App</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        input, button { margin: 5px; }
        #goalList, #schemeResults { margin-top: 10px; }
    </style>
</head>
<body>

<h1>Women's Empowerment and Safety App</h1>

<h2>Health Goals</h2>
<input type="text" id="goalInput" placeholder="Enter a health goal">
<button onclick="addGoal()">Add Goal</button>

<h3>Your Goals</h3>
<ul id="goalList"></ul>

<label for="progressInput">Progress (%):</label>
<input type="number" id="progressInput" min="0" max="100">
<button onclick="updateProgress()">Update Progress</button>

<h2>Government Schemes</h2>
<input type="text" id="schemeSearchInput" placeholder="Search for schemes">
<button onclick="searchScheme()">Search Schemes</button>

<h3>Search Results</h3>
<pre id="schemeResults"></pre>

<script>
    const MAX_GOALS = 10;
    const goals = [];
    const schemes = [
        { name: "Maternity Benefit Scheme", description: "Financial support for mothers.", eligibility: "For expecting mothers." },
        { name: "Women Entrepreneurship Program", description: "Support for women starting a business.", eligibility: "Women entrepreneurs." }
    ];

    function addGoal() {
        const goalInput = document.getElementById('goalInput');
        const goalText = goalInput.value.trim();

        if (goalText && goals.length < MAX_GOALS) {
            goals.push({ goal: goalText, progress: 0 });
            updateGoalList();
            alert(Goal added: ${goalText});
            goalInput.value = '';
        } else {
            alert("Goal cannot be empty or maximum goals reached.");
        }
    }

    function updateProgress() {
        const progressInput = document.getElementById('progressInput');
        const progress = parseInt(progressInput.value);
        const goalList = document.getElementById('goalList');
        const selectedGoalIndex = goalList.selectedIndex;

        if (selectedGoalIndex !== -1 && !isNaN(progress) && progress >= 0 && progress <= 100) {
            goals[selectedGoalIndex].progress = progress;
            updateGoalList();
            alert(Progress updated to ${progress}%);
        } else {
            alert("Please select a goal to update progress and enter a valid progress (0-100).");
        }
    }

    function updateGoalList() {
        const goalList = document.getElementById('goalList');
        goalList.innerHTML = '';
        goals.forEach((goal, index) => {
            const li = document.createElement('li');
            li.textContent = ${goal.goal}: ${goal.progress}%;
            goalList.appendChild(li);
        });
    }

    function searchScheme() {
        const keyword = document.getElementById('schemeSearchInput').value.trim().toLowerCase();
        const results = schemes.filter(scheme => 
            scheme.name.toLowerCase().includes(keyword) || 
            scheme.description.toLowerCase().includes(keyword)
        );

        const schemeResults = document.getElementById('schemeResults');
        schemeResults.textContent = results.length ? results.map(scheme => 
            Scheme: ${scheme.name}\nDescription: ${scheme.description}\nEligibility: ${scheme.eligibility}\n
        ).join('\n') : "No matching schemes found.";
    }
</script>

</body>
</html>
