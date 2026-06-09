#!/usr/bin/env python3
"""
Generate all 12 Tarnas course lectures as MP3 files using ElevenLabs API.
Run: python3 generate_lectures.py
Output: ~/tarnas-course/audio/lecture_01.mp3 ... lecture_12.mp3
"""

import os
import sys
import json
import urllib.request
import urllib.error

API_KEY = os.environ.get("ELEVENLABS_API_KEY")
VOICE_ID = "6fZce9LFNG3iEITDfqZZ"
OUTPUT_DIR = os.path.expanduser("~/tarnas-course/audio")

if not API_KEY:
    print("ERROR: ELEVENLABS_API_KEY not set.")
    print("Run: export ELEVENLABS_API_KEY=\"your-key-here\"")
    sys.exit(1)

os.makedirs(OUTPUT_DIR, exist_ok=True)

LECTURES = [
    ("01", "Who Is Richard Tarnas?", """Welcome to Cosmos and Psyche: An Audio Course in the Astrological Work of Richard Tarnas.

Lecture One: Who Is Richard Tarnas?

Before engaging with Tarnas's ideas, it is worth understanding who he actually is — because the usual mental image conjured by the word "astrologer" is not accurate here.

Richard Theodore Tarnas was born in 1950 in Geneva, Switzerland. He entered Harvard University in 1968 and graduated cum laude in 1972. He completed a PhD at Saybrook Institute in 1976, with a thesis focused on psychedelic therapy and the theoretical implications of LSD research for psychology.

In 1974, he traveled to Esalen Institute in Big Sur, California, to study with the Czech-American psychiatrist Stanislav Grof — one of the twentieth century's leading researchers into non-ordinary states of consciousness. Tarnas would remain at Esalen for a decade, eventually serving as its director of programs. During those years, his intellectual companions included Joseph Campbell, Gregory Bateson, Elizabeth Kübler-Ross, and James Hillman — a constellation of thinkers working at the intersection of depth psychology, mythology, and a critique of scientific rationalism.

Tarnas left Esalen in 1984 and spent the next six years writing what would become his first book: The Passion of the Western Mind. Published in 1991, it became a bestseller and remained in use at universities for decades. It contains no astrology whatsoever. It is simply a masterful narrative history of Western thought — from ancient Greece through postmodernism — praised by Joseph Campbell and widely regarded as one of the finest intellectual histories of its kind.

Only after that — only after establishing this scholarly foundation — did Tarnas publish his explicitly astrological work: Prometheus the Awakener in 1995, and Cosmos and Psyche in 2006, the result of thirty years of research.

This sequence matters. Tarnas is not a believer-first astrologer reaching for intellectual respectability. He is a historian and philosopher who subjected an anomalous hypothesis to three decades of scrutiny before presenting it publicly. Whether his conclusions hold is a separate question. But the character of his inquiry is serious, and it deserves serious engagement.

He is currently Professor Emeritus at the California Institute of Integral Studies in San Francisco, and founding director of its graduate program in Philosophy, Cosmology, and Consciousness."""),

    ("02", "The Passion of the Western Mind", """Lecture Two: The Passion of the Western Mind — The Necessary Prologue.

The Passion of the Western Mind, published in 1991, is where any serious engagement with Tarnas must begin.

The book is a narrative history of Western thought, moving from Homeric cosmology through ancient Greece, the rise of Christianity, the medieval synthesis, the Scientific Revolution, the Enlightenment, Romanticism, Nietzsche, Freud, and into the fragmented twentieth century. It traces, with unusual clarity and sympathy, how Western human beings came to understand themselves and their place in the universe.

What Tarnas shows — and this is the book's central argument — is that the modern world arrived at its current condition through a specific intellectual arc. The ancient world understood itself as embedded in a living, meaningful cosmos. The Scientific Revolution, whatever its extraordinary achievements, produced what the philosopher Max Weber called the disenchantment of the world: the universe became a mechanism, not a home; matter became inert, not sacred; and the human being became an isolated consciousness looking out at a dead universe that has no intrinsic meaning to offer.

Tarnas does not romanticize the pre-modern world or dismiss science. His critique is more precise: the problem is not scientific method but a particular metaphysical assumption — the sharp Cartesian division between the knowing subject and the known world — that was elevated from a useful methodological stance into a metaphysical absolute.

The Epilogue to the book, titled "The Transformation of the Western Mind," is where Tarnas first gestures toward his proposed resolution. He argues that the Western mind's trajectory is not the end of the story. It is a developmental passage — from embedded participation in a sacred cosmos, to radical alienation, toward an adult capacity for genuine differentiated relationship.

The future he gestures toward is a participatory epistemology: one in which the human mind is understood not as a passive receptor of external data, but as an active co-participant with a world that itself has depths of meaning.

For the skeptic: this book stands completely on its own, independent of any astrological claims. It is simply one of the best single-volume histories of Western ideas ever written. Read it first."""),

    ("03", "What Is an Archetype?", """Lecture Three: What Is an Archetype?

Before anything else in Tarnas's astrological work can be properly evaluated, one concept must be understood: the archetype. Not as a psychological buzzword or a Jungian cliché, but as a specific philosophical tradition with a two-and-a-half-thousand-year history.

The concept begins with Plato. For Plato, archetypes — or Forms — are the universal patterns from which all particular things in the world are derived. The Form of Beauty is not beautiful in the way a rose is beautiful; it is the universal structure of beauty itself, which particular beautiful things imperfectly instantiate. This is a serious metaphysical claim: the world's particular appearances are grounded in universal, immaterial, eternally existing patterns.

Carl Jung gave the concept its modern psychological form. For Jung, archetypes are universal patterns embedded in what he called the collective unconscious — a layer of the psyche shared across all humanity, not derived from individual experience. The archetypes manifest as recurring figures in dreams, myths, and art across cultures: the Hero, the Great Mother, the Shadow, the Self, the Trickster.

James Hillman, building on Jung, pushed this further in what he called archetypal psychology. For Hillman, the archetypes are not just psychological categories but the organizing principles of experience — the gods, in polytheistic imagination, are names for the fundamental modes in which reality shows up for us.

Tarnas synthesizes all of this. His claim is not that the planets cause archetypes to manifest, nor that the archetypes exist solely inside the human mind. His claim is more radical and more philosophically interesting: the planetary archetypes are universal patterns that manifest simultaneously in the outer world and the inner world — not because one causes the other, but because mind and cosmos are not ultimately separate.

This is the epistemological leap at the heart of his work. You don't have to accept it — but you need to understand it to evaluate the argument."""),

    ("04", "The Planetary Archetypes", """Lecture Four: The Planetary Archetypes — A Symbolic Dictionary.

Tarnas works primarily with the outer planets — those beyond Saturn — because their slow movement through the zodiac means that their angular relationships to each other last for years or even decades, creating what astrologers call world transits that he correlates with large-scale cultural and historical periods.

Let us walk through the core archetypes as Tarnas defines them.

Saturn. The archetype of structure, limitation, time, and maturation. Saturn represents the principle of necessity — the hard facts that constrain us, the weight of karma, the reality principle. In mythology, Saturn is Kronos: father of time, devourer of his children, lord of limitation.

Uranus — or as Tarnas prefers, Prometheus. The planet traditionally called Uranus carries the archetypal signature not of the mythological sky god Uranus but of Prometheus — the Titan who stole fire from the gods. The archetype is one of liberation, sudden awakening, rebellion, technological innovation, the breaking of old forms, and Promethean fire — the spark that disrupts the status quo.

Neptune. The archetype of dissolution, mysticism, idealism, the oceanic, spiritual longing, and illusion. Neptune dissolves boundaries — between self and other, between the real and the imagined, between the sacred and the mundane. In its shadow: confusion, delusion, escapism.

Pluto. The most intense and concentrated of the outer planetary archetypes. Pluto is the principle of depth, transformation, power, compulsion, death and rebirth. Named for the lord of the underworld, the Plutonic archetype manifests as volcanic eruptions of what had been buried — in individuals, as shadow material demanding integration; in history, as revolutionary upheaval.

The crucial point: Tarnas does not use these archetypes as rigid categories. He insists they are more like musical themes that can be played in many keys — the same planetary archetype can manifest as liberation or as chaos, as spiritual vision or as delusion, depending on the broader context."""),

    ("05", "Cosmos and Psyche — The Central Argument", """Lecture Five: Cosmos and Psyche — The Central Argument.

Published in 2006 by Viking Press, Cosmos and Psyche: Intimations of a New World View is Richard Tarnas's primary scholarly statement. It is the result of thirty years of research.

The central claim is this: major events and cultural shifts in Western history correlate — consistently, meaningfully, and across multiple independent cases — with the angular relationships between the outer planets as observed from Earth. Specifically, when planets like Uranus, Neptune, and Pluto form significant angular alignments — conjunctions, oppositions, squares — the cultural and historical character of those periods reflects the archetypal qualities associated with those planets.

This is not a claim about individual natal charts. Tarnas is making a claim about world history — about why the 1960s were the 1960s, why the French Revolution happened when it did, why the Romantic era had its distinctive character.

The book documents these claims through a series of detailed historical case studies. The Uranus-Pluto conjunction of the mid-1960s: a period of revolutionary cultural upheaval, liberation movements, and the dismantling of established social structures. The Saturn-Pluto conjunction of 1914: the outbreak of World War One, the collapse of the old European order. The alignment of Uranus and Neptune in the late eighteenth and early nineteenth centuries: the Romantic era, a period of spiritual idealism and the revolt against Enlightenment rationalism.

Tarnas also applies the framework to individual biographies — following the planetary transits in the lives of Nietzsche, Freud, Darwin, and Beethoven, finding that major creative breakthroughs or personal crises correlate with specific planetary configurations.

His methodology is explicitly historical and interpretive, not statistical. He argues that the sheer weight of convergent evidence constitutes a meaningful pattern that cannot be explained by coincidence alone.

His epistemological position is carefully qualified. He does not claim that the planets cause historical events. He claims something more modest and more philosophically interesting: that the cosmos is meaningfully patterned, and that planetary positions serve as a kind of symbolic clock — not a causal mechanism but a correlative signature of archetypal currents that are already running through reality."""),

    ("06", "Prometheus the Awakener", """Lecture Six: Prometheus the Awakener — The Uranus Problem.

Prometheus the Awakener, published in 1995 by Spring Publications, is a lean, focused essay of about a hundred pages. It addresses a specific scholarly problem that sits at the heart of Tarnas's broader project.

The problem is this. In 1781, the astronomer William Herschel discovered a new planet beyond Saturn. It was eventually named Uranus after the Greek sky god — the primordial heaven, father of the Titans, castrated by his son Cronus and deposed from power.

But as astrologers began working with the new planet over the following two centuries, they found that its actual astrological signature had almost nothing to do with the mythological Uranus. The sky god Uranus is associated with the status quo, with primordial authority. The planet's actual signature was precisely the opposite: sudden liberation, revolutionary change, the spark of Promethean fire, the awakener who disrupts sleeping consciousness, the trickster who breaks old forms to usher in the new. This is not Uranus. This is Prometheus.

Tarnas makes the case in elegant detail. The Prometheus myth: the Titan who stole fire from the gods and gave it to humanity, enabling civilization, technology, and consciousness. Who was punished by Zeus for this act of transgressive liberation.

The planet Uranus was discovered in 1781 — at the precise historical moment of the American and French Revolutions, the beginning of the Industrial Revolution, the Romantic movement's revolt against Enlightenment rationalism. All of these are Promethean themes: the theft of political power from the gods of the old order, the gift of fire to common humanity, the birth of a new era of consciousness.

Tarnas argues this is not coincidence. It is the same pattern — the Promethean archetype — manifesting simultaneously in political history, cultural life, and the symbolic moment of the planet's discovery."""),

    ("07", "The Best Objections", """Lecture Seven: The Best Objections — How to Push Back Seriously.

When the Wall Street Journal reviewed Cosmos and Psyche in 2006, the reviewer compared it to Newton's later alchemical writings — implying senility rather than engaging the argument. That is not a critique; it is a dismissal. Tarnas deserves better opposition than that, because the genuine objections are philosophically interesting.

Let us work through them clearly.

The first and most significant is the confirmation bias problem. Tarnas selects which historical events to examine. In a work covering five centuries of Western history, there are an enormous number of events to choose from. A skeptic must ask: is Tarnas selecting the events that fit his planetary correlations and ignoring or underweighting those that do not? A systematic quantitative study — which Tarnas does not provide — would be more convincing.

The second objection is the interpretive flexibility problem. Each planetary archetype is defined broadly enough that it could be invoked to explain almost any major historical development. Pluto is transformation, power, death and rebirth. Uranus-Prometheus is liberation, awakening, revolution, disruption. Given these definitions, virtually any significant historical event involves one or the other. The theory may be, in Karl Popper's term, unfalsifiable in practice.

The third objection is the mechanism problem. Tarnas explicitly disclaims any causal mechanism. He does not claim the planets exert gravitational or electromagnetic effects on human consciousness or history. He claims correlation without mechanism. The framework he invokes for this is Jung's concept of synchronicity — but synchronicity is itself deeply contested.

What Tarnas actually claims, in his most careful formulations, is modest: that the cosmos appears to be meaningfully patterned; that this patterning resonates with human history in ways that are statistically improbable if purely coincidental; and that this constitutes evidence — not proof — for a participatory view of the universe. He explicitly acknowledges that he could be wrong.

The intellectually honest position is this: the case studies are impressive and the historical correlations are often striking. The methodological foundations are genuinely weak. The philosophical implications, if the correlations hold, would be profound. Serious engagement means holding all three of these things simultaneously."""),

    ("08", "Tarnas in the Intellectual Ecosystem", """Lecture Eight: Tarnas in the Intellectual Ecosystem.

No thinker exists in isolation. To understand Tarnas properly, it helps to map the intellectual community from which he emerged.

The most important figure in Tarnas's intellectual formation is Stanislav Grof. Grof is a Czech-American psychiatrist who, beginning in the 1950s, conducted extensive clinical research into non-ordinary states of consciousness — first using LSD in carefully controlled therapeutic settings, later developing Holotropic Breathwork as a drug-free alternative. His research produced detailed phenomenological maps of the psyche's depths, including what he called transpersonal states: experiences that seem to transcend the individual ego and access something wider — mythological imagery, collective memory, cosmic consciousness.

Grof's work is significant for Tarnas in two ways. First, it provided empirical evidence — clinical, not merely philosophical — that the psyche has depths that the standard Western model of consciousness does not adequately account for. Second, Grof's maps of the psyche's depths are organized around archetypal structures that correspond directly to the planetary archetypes Tarnas uses in his astrological work. Grof found, independently and through clinical observation, that the same symbolic complexes appeared consistently in his patients' deepest experiences. This convergence is, for Tarnas, significant independent corroboration.

James Hillman, the Jungian psychologist who founded archetypal psychology, is the other central influence. Hillman argued that psychology had become too focused on the individual ego's development and needed to recover a sense of the soul as embedded in a larger world of images and stories.

Jorge Ferrer, a philosopher of religion, provides Tarnas's epistemological framework. Ferrer's participatory theory of spirituality argues that genuine spiritual knowledge arises through the participation of the human being and the world in a shared event of disclosure. Reality itself, in this view, is not merely what the individual mind projects onto a neutral substrate; it is something that reveals itself through the act of participation."""),

    ("09", "Recommended Reading Path", """Lecture Nine: Recommended Reading Path.

Having surveyed the intellectual landscape of Tarnas's work, let me recommend how to actually read it — in what order, with what expectations, and with what questions in mind.

Begin with The Passion of the Western Mind. Read it before anything else. If you have limited time, read at least the Epilogue, which runs about twenty-five pages. This is the foundation. Without it, the philosophical motivation for Cosmos and Psyche is opaque.

As you read The Passion of the Western Mind, pay particular attention to Tarnas's account of the Scientific Revolution — not as a critique of science, but as a history of a particular metaphysical move: the elevation of the Cartesian subject-object divide from a useful methodological tool to an absolute metaphysical principle. This is the problem his later work is a response to.

Second, read Prometheus the Awakener. It is short — about a hundred pages — and it is the best introduction to how Tarnas actually works with a single planetary archetype. It is more precise and more testable than the broader historical claims of Cosmos and Psyche.

Third, read Cosmos and Psyche. Do not skip the Introduction and Part One, which lay out the philosophical foundations. The historical case studies in Parts Two through Five are where the real work is done. The case study on the 1960s, which Tarnas analyzes through the Uranus-Pluto conjunction of 1965 to 1966, is particularly vivid and well-argued.

Fourth, as a philosophical supplement, read Jung's Synchronicity: An Acausal Connecting Principle, published in 1952. Understanding synchronicity in Jung's original formulation will help you assess whether Tarnas is using it carefully or leaning on it as a conceptual escape hatch.

Fifth, for the psychological background, James Hillman's Re-Visioning Psychology from 1975 gives you the archetypal psychology tradition in its most elegant form."""),

    ("10", "Questions to Hold While Reading", """Lecture Ten: Questions to Hold While Reading — A Framework for Active Engagement.

This final lecture offers not conclusions but questions — the questions that will help you engage with Tarnas seriously rather than either dismissing him or accepting him uncritically.

The first question: What exactly is being claimed? Tarnas makes several distinct claims that need to be evaluated separately. There is the empirical claim — that historical events correlate with planetary positions. There is the explanatory claim — that this correlation reflects a meaningful pattern in the cosmos. There is the philosophical claim — that this supports a participatory view of the universe. And there is the practical claim — that astrological analysis can offer genuine insight into personal and historical experience. These claims do not stand or fall together.

The second question: What would count as disconfirming evidence? Ask yourself seriously: is there any configuration of historical evidence that would lead Tarnas to abandon his theory? If the archetypes are defined broadly enough to explain anything, the theory cannot be falsified. This is not necessarily a fatal objection — philosophy is not science — but it is a question worth pressing.

The third question: Is the participatory epistemology a genuine philosophical position, or a rhetorical move to pre-empt criticism? Tarnas argues that the sharp distinction between subjective meaning and objective fact is itself a product of a particular historical metaphysics that may be wrong. This is a philosophically serious argument. But it can also function as a way of declaring the normal rules of evidence inapplicable.

The fourth question: Does the quality of the historical analysis depend on the astrological framework? The case studies in Cosmos and Psyche are often genuinely illuminating as intellectual history, independent of any astrological conclusions. What is the astrological layer actually adding?

The fifth question: What is the personal meaning of this inquiry for you? Tarnas is not merely offering a theory of history. He is offering a framework for understanding one's own life as embedded in larger cosmic patterns. There is nothing wrong with this. But it is worth being honest about whether you are evaluating the theory or being drawn by the experience."""),

    ("11", "The World Transits of Our Moment", """Lecture Eleven: The World Transits of Our Moment.

This lecture draws directly from the archetypal weather report Tarnas delivered live at CIIS in February 2024 — the most recent of a series he has given since 2020. These are his words, his examples, and his framing, rendered here as closely as possible to how he actually speaks.

He opened with a characteristic note of philosophical honesty. The planets, he said, do not operate in a linear causal mechanistic way. He prefers to understand the phenomenon through the language that Plotinus and Jung both use: synchronicity. Not that the planets cause what happens on Earth, but that there is an ongoing correspondence — a correlation — between the movements of the planets and the movements of the archetypal dynamics of human experience. Everything is interconnected, as Plotinus put it: all things breathe together. Everything is symbolically meaningful.

He was also explicit that the framework is not deterministic. The more consciousness we bring to the table — the more self-awareness, courage, intelligence, and imagination — the more freedom and skillfulness we can bring to participating in the archetypal forces moving through and around us.

On Jupiter-Uranus: he called this probably the most fun among the outer planetary combinations, with the greatest buoyancy. The historical correlations across the centuries are, in his word, dazzling. The history of quantum physics is remarkably connected to this cycle: Max Planck's foundational work in 1900, then Bohr's principle of complementarity and Heisenberg's uncertainty principle in the late 1920s, both under Jupiter-Uranus conjunctions. Beethoven's Eroica Symphony. Joni Mitchell's first albums. The fall of the Berlin Wall. The moon landing. Steve Jobs and Steve Wozniak beginning their work in a garage in Palo Alto — a hidden birth, nobody knowing at the time what would come of it.

On Saturn-Neptune, entering its major phase through 2025 and 2026: this is a more sobering and complex combination. At its best: extraordinary for focused consciousness, nuanced awareness, psychological depth, and spiritual practice. He invoked the Dalai Lama and Martin Luther King — people who faced the loss of the ideal and responded with sustained effort to bring the dream into concrete, costly, sustained expression.

He then turned to the American dimension. The United States is going through two simultaneous returns — its Pluto return, the first in the nation's history, and its Uranus return, the third, since Uranus completes its cycle in 84 years. The first American Uranus return coincided with the Civil War. The second with World War Two and the emergence of the US as a global superpower. We are now at the beginning of the third.

He ended with a passage from Tolkien. Frodo says to Gandalf: I wish it need not have happened in my time. And Gandalf replies: So do I, and so do all who live to see such times. But that is not for them to decide. All we have to decide is what to do with the time that is given us.

That, he said, is where we are."""),

    ("12", "How to Use This in Your Own Life", """Lecture Twelve: How to Use This in Your Own Life — Personal Transits and Conscious Participation.

Tarnas is consistently asked what people should actually do with this material. This lecture addresses that question directly.

The first distinction he always makes is between world transits and personal transits. World transits — Jupiter-Uranus, Saturn-Neptune, the American Pluto and Uranus returns — describe the archetypal field that everyone on Earth is living inside, regardless of when they were born. They are like the weather of the era. Personal transits describe how the currently moving planets are interacting with the specific positions of the planets at the moment of your birth. Both matter. The world transit sets the field; your personal transit determines your particular relationship to it.

With that distinction in place, he offered some concrete guidance about what the current world transits call for in individual lives.

During a Jupiter-Uranus conjunction, the advice he gave was unusually direct. If you have been thinking about starting a creative project, this is the time. If you have been gestating something — a book, a dissertation, a new direction in your work — this is the period when the archetypal field is most supportive of bringing it forward. He said directly: you don't want to sleep through it. The shadow is inflation; bring discernment with the enthusiasm. But use the wind.

During a Saturn-Neptune conjunction, the call is different. This is a period when more people feel the pull toward psychotherapy, toward spiritual practice, toward the kind of serious inner work that requires sustained commitment. The people who thrive in this period, historically, are those who can hold both the real and the ideal — who work hard and seriously in service of something that matters spiritually.

The deeper point Tarnas returns to again and again is the difference between being unconscious of the archetypal field you are in — being, in his phrase, a puppet of the archetypal powers — and being a conscious participant in it. He is not calling for mastery or control of the archetypes. He is calling for awareness: knowing the kind of weather you are in so you can move within it with skill and intentionality.

He closed with a thought about what the symbolic intelligibility of the cosmos means at the deepest level. We are capable of this discernment — of reading the moving geometry of the solar system as a meaningful language — and that capacity is not, in his view, accidental. It speaks to something about the relationship between the cosmos and the human mind. The language of the soul of the world is a language the human soul can read. That is the most fundamental claim of his entire life's work. Not certainty. But an invitation: take your symbolic capacities seriously, develop them, and bring them to bear on the extraordinary moment we are all living in together."""),
]

def generate_lecture(num, title, text):
    output_path = os.path.join(OUTPUT_DIR, f"lecture_{num}.mp3")
    if os.path.exists(output_path):
        print(f"  [{num}] Already exists, skipping.")
        return True

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    payload = json.dumps({
        "text": text,
        "model_id": "eleven_turbo_v2_5",
        "voice_settings": {
            "stability": 0.45,
            "similarity_boost": 0.82,
            "style": 0.15,
            "use_speaker_boost": True
        }
    }).encode("utf-8")

    req = urllib.request.Request(url, data=payload, headers={
        "xi-api-key": API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg"
    })

    try:
        with urllib.request.urlopen(req) as response:
            audio_data = response.read()
        with open(output_path, "wb") as f:
            f.write(audio_data)
        size_kb = len(audio_data) // 1024
        print(f"  [{num}] {title} — {size_kb}KB saved.")
        return True
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"  [{num}] ERROR {e.code}: {body}")
        return False
    except Exception as e:
        print(f"  [{num}] ERROR: {e}")
        return False

print(f"\nGenerating {len(LECTURES)} lectures → {OUTPUT_DIR}\n")

success = 0
for num, title, text in LECTURES:
    if generate_lecture(num, title, text):
        success += 1

print(f"\nDone. {success}/{len(LECTURES)} lectures generated.")
print(f"Files are in: {OUTPUT_DIR}")
