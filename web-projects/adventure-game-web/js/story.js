let state = {}

// Game Path

const gameArray = [{
        id: 1,
        text: 'Now choose a rank',
        options: [{
                text: 'Knight',
                setState: {
                    Knight: true
                },
                nextText: 2
            },
            {
                text: 'Lady',
                setState: {
                    Lady: true
                },
                nextText: 2
            },
            {
                text: 'Lord',
                setState: {
                    Lord: true
                },
                nextText: 2
            },
            {
                text: 'Squire',
                setState: {
                    Squire: true
                },
                nextText: 2
            },
            {
                text: 'Villager',
                setState: {
                    Villager: true
                },
                nextText: 2
            },
            {
                text: 'Witch',
                setState: {
                    Witch: true
                },
                nextText: 2
            },
            {
                text: 'Wizard',
                setState: {
                    Wizard: true
                },
                nextText: 2
            }
        ]
    },
    {
        id: 2,
        text: 'Greetings weary traveller',
        options: [{
            text: 'Start',
            nextText: 3
        }]
    },

]