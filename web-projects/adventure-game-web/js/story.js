let state = {}

// Game Path

const textNodes = [{
        id: 1,
        text: 'You see a bag and some items on a table You pick up the bag and:',
        options: [{
                text: 'beans',
                setState: { beans: true },
                nextText: 2
            },
            {
                text: 'apple',
                setState: { apple: true },
                nextText: 2
            },
            {
                text: 'sword',
                setState: { sword: true },
                nextText: 2
            },
            {
                text: 'wand',
                setState: { wand: true },
                nextText: 2
            }
        ]
    },
    {
        id: 2,
        text: 'You leave the house.',
        options: [{
            text: 'Restart',
            nextText: -1
        }]
    }
]