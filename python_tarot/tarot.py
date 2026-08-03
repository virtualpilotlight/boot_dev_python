import random

all_cards = [
    ["|0| - the fool - upright - folly, mania, extravagance, intoxication, delirium, frenzy, bewrayment.", "|0| - the fool - inverted - negligence, absence, distribution, carelessness, apathy, nullity, vanity."],
    ["|i| - the magician - upright - energy, potential, and the manifestation of one's desires", "|i| - the magician - inverted - unfocused, unmanifested, madness, mental distress"],
    ["|ii| - the high priestess - upright - secrets, mystery, silence, tenacity, mystery, wisdom, science.", "|ii| - the high priestess - inverted - passion, moral or physical ardor, conceit, surface knowledge."],
    ["|iii| - the empress - upright - fruitfulness, action, initiative, the unknown, clandestine, difficulty, doubt, ignorance.", "|iii| - the empress - inverted - light, truth, public rejoicings, vacillation."],
    ["|iv| - the emperor - upright - stability, power, protection, logic, realization, a great person, aid, reason, conviction, authority, will", "|iv| - the emperor - inverted - benevolence, compassion, credit, confusion to enemies, obstruction, immaturity."],
    ["|v| -the hierophant - upright - marriage, alliance, captivity, servitude, mercy, and goodness, inspiration.", "|v| -the hierophant - inverted - society, good understanding, concord, over kindness, weakness."],
    ["|vi| - the lovers - upright - attraction, love, beauty, trials overcome.", "|vi| - the lovers - inverted - failure, foolish designs, contrarieties."],
    ["|vii| - the chariot - upright - succour, providence, also war, triumph, presumption, vengeance, trouble.", "|vii| - the chariot - inverted - riot, quarrel, dispute, litigation, defeat."],
    ["|viii| - fortitude - upright - power, energy, action, courage, magnanimity, success with honours.", "|viii| - fortitude - inverted - despotism, abuse of power, weakness, discord, disgrace."],
    ["|ix| - the hermit - upright - Prudence, circumspection, treason, dissimulation, roguery, corruption.", "|ix| - the hermit - inverted -  concealment, disguise, policy fear, unreasoned caution."],
    ["|x| - wheel of fortune - upright - destiny, fortune, success, elevation, luck, felicity.", "|x| - wheel of fortune - inverted -  increase, abundance, superfluity."],
    ["|xi| - justice - upright - equity, rightness, probity, executive.", "|xi| - justice - inverted -  law, legal complications, bigotry, bias, excessive severity."],
    ["|xii| - the hanged man - upright - wisdom, circumspection, discernment, trials, sacrifice, intuition, divination, prophecy.", "|xii| - the hanged man - inverted - selfishness, the crowd, body politic."],
    ["|xiii| - death - upright - end, mortality, destruction, corruption, many contrarieties", "|xiii| - death - inverted -  inertia, sleep, lethargy, petrifaction, somnambulism, hope destroyed."],
    ["|xiv| - temperance - upright - economy, moderation, frugality, management, accommodation.", "|xiv| - temperance - inverted - disunion, unfortunate combinations, competing interests."],
    ["|xv| - the devil - upright - ravage, violence, vehemence, extraordinary efforts, force, fatality.", "|xv| - the devil - inverted - evil fatality, weakness, pettiness, blindness."],
    ["|xvi| - the tower - upright -  misery, distress, indigence, adversity, calamity, disgrace, deception, ruin, unforeseen catastrophe.", "|xvi| - the tower - inverted - negligence, absence, distribution, carelessness, distraction, apathy, nullity, vanity."],
    ["|xvii| - the star - upright - Hope and bright prospects.", "|xvii| - the star - inverted - Loss, theft, privation, abandonment, arrogance, haughtiness, impotence."],
    ["|xviii| - the moon - upright - Hidden enemies, danger, calumny, darkness, terror, deception, occult forces, error.", "|xviii| - the moon - inverted -  instability, inconstancy, silence, less deception & error."],
    ["|xix| - the sun - upright - accomplishment, material happiness, contentment.", "|xix| - the sun - inverted - lucky!"],
    ["|xx| - judgment - upright - judgement, rebirth, inner-calling, absolution.", "|xx| - judgment - inverted- karma, causality, second chance."],
    ["|xxi| - the world - upright - success, recompense, voyage, route, emigration, flight.", "|xxi| - the world - inverted -  inertia, fixity, stagnation, permanence."],
    ["|ap| - ace of penticles - upright - wealth, potential.", "|a| - ace of penticles - inverted - loss, confusion"],
    ["|2p| - two of penticles - upright -juggle, balance, maintainance.", "|2| - two of penticles - inverted - imbalances, struggling"],
    ["|3p| - three of penticles - upright -  mastery of a skill, achieving perfection, artistic ability", "|3| - three of penticles - inverted - sloppiness,  lack of skill, banal ideas."],
    ["|4p| - four of penticles - upright - greed, hoarding", "|4| - four of penticles - inverted - spendthriftiness."],
    ["|5p| - five of penticles - upright - loss of faith,  losing security.", "|5| - five of penticles - inverted -  hope returns, renewal of faith."],
    ["|6p| - six of penticles - upright - redistribution of gratification, questions the motives of charity.", "|6| - six of penticles - inverted -  desire, cupidity, envy, jealousy, illusion."],
    ["|7p| - seven of penticles - upright - movement,  commitment towards your dreams, emotional and spiritual rewards.", "|7| - seven of penticles - inverted - doing too much, cut your losses, bad investment."],
    ["|8p| - eight of penticles - upright - work, employment, commission, craftsmanship, skill in business, preparatory stage", "|8| - eight of penticles - inverted - voided ambition, vanity, cupidity, exaction, usury."],
    ["|9p| - nine of penticles - upright - financial independence,  treat yourself, stable financial plateau.", "|9| - nine of penticles - inverted -  excess spending, being co-dependent."],
    ["|10p| - ten of penticles - upright - family matters, financial matters, affluence.", "|10| - ten of penticles - inverted - the dark side of wealth, financial failure, loss."],
    ["|pp| - page of pentacles - upright - young person, changing of your line of work, more responsibility.", "|p| - page of pentacles - inverted -  lack of progress, procrastination, learn from failure."],
    ["|jp| - jack of penticles - upright - hard work, productivity, routine, conservatism.", "|j| - jack of penticles - inverted - self-discipline, boredom, feeling 'stuck', perfectionism."],
    ["|kp| - king of penticles - upright - wealth, business, leadership, security, discipline, abundance.", "|k| - king of penticles - inverted - financially inept, obsessed with wealth and status, stubborn."],
    ["|qp| - queen of penticles - upright - nurturing, practical, providing financially.", "|q| - queen of penticles - inverted- Financial independence, self-care, work-home conflict."],
    ["|as| - ace of swords - upright - breakthroughs, new ideas, mental clarity, success.", "|a| - ace of swords - inverted - inner clarity, re-thinking an idea, clouded judgement."],
    ["|2s| - two of swords - upright - difficult decisions, weighing up options, an impasse, avoidance", "|2| - two of swords - inverted - indecision, confusion, information overload, stalemate."],
    ["|3s| - three of swords - upright - heartbreak, emotional pain, sorrow, grief, hurt.", "|3| - three of swords - inverted - negative self-talk, releasing pain, optimism, forgiveness."],
    ["|4s| - four of swords - upright - rest, relaxation, meditation, contemplation, recuperation", "|4| - four of swords - inverted - exhaustion, burn-out, deep contemplation, stagnation"],
    ["|5s| - five of swords - upright - conflict, disagreements, competition, defeat, winning at all costs.", "|5| - five of swords - inverted - reconciliation, making amends, past resentment."],
    ["|6s| - six of swords - upright - transition, change, rite of passage, releasing baggage.", "|6| - six of swords - inverted - personal transition, resistance to change, unfinished business."],
    ["|7s| - seven of swords - upright - betrayal, deception, getting away with something, acting strategically.", "|7| - seven of swords - inverted - imposter syndrome, self-deceit, keeping secrets."],
    ["|8s| - eight of swords - upright - negative thoughts, self-imposed restriction, imprisonment, victim mentality.", "|8| - eight of swords - inverted - self-limiting beliefs, inner critic, releasing negative thoughts, open to new perspectives."],
    ["|9s| - nine of swords - upright - anxiety, worry, fear, depression, nightmares.", "|9| - nine of swords - inverted - inner turmoil, deep-seated fears, secrets, releasing worry."],
    ["|10s| - ten of swords - upright - painful endings, deep wounds, betrayal, loss, crisis", "|10| - ten of swords - inverted - recovery, regeneration, resisting an inevitable end."],
    ["|ps| - page of swords - upright - new ideas, curiosity, thirst for knowledge, new ways of communicating", "|p| - page of swords - inverted - self-expression, all talk and no action, haphazard action, haste."],
    ["|js| - jack of swords - upright - ambitious, action-oriented, driven to succeed, fast-thinking.", "|j| - jack of swords - inverted - restless, unfocused, impulsive, burn-out."],
    ["|ks| - king of swords - upright - mental clarity, intellectual power, authority, truth.", "|k| - king of swords - inverted - quiet power, inner truth, misuse of power, manipulation."],
    ["|qs| - queen of swords - upright -  independent, unbiased judgement, clear boundaries, direct communication.", "|q| - queen of swords - inverted -  overly-emotional, easily influenced, bitchy, cold-hearted."],
    ["|aw| - ace of wands - upright - inspiration, new opportunities, growth, potential.", "|a| - ace of wands - inverted - an emerging idea, lack of direction, distractions, delays."],
    ["|2w| - two of wands - upright - future planning, progress, decisions, discovery.", "|2| - two of wands - inverted - personal goals, inner alignment, fear of unknown, lack of planning."],
    ["|3w| - three of wands - upright - progress, expansion, foresight.", "|3| - three of wands - inverted - playing small, lack of foresight, unexpected delays."],
    ["|4w| - four of wands - upright - celebration, joy, harmony, relaxation, homecoming.", "|4| - four of wands - inverted - personal celebration, inner harmony, conflict with others, transition."],
    ["|5w| - five of wands - upright - conflict, disagreements, competition, tension.", "|5| - five of wands - inverted - inner conflict, conflict avoidance, tension release, adversity."],
    ["|6w| - six of wands - upright - success, public recognition, progress, self-confidence.", "|6| - six of wands - inverted - private achievement, personal definition of success, fall from grace, egotism."],
    ["|7w| - seven of wands - upright - challenge, competition, protection, perseverance.", "|7| - seven of wands - inverted - exhaustion, giving up, overwhelmed."],
    ["|8w| - eight of wands - upright - movement, fast paced change, action, alignment, air travel.", "|8| - eight of wands - inverted - delays, frustration, resisting change, internal alignment."],
    ["|9w| - nine of wands - upright - resilience, courage, persistence, test of faith, boundaries.", "|9| - nine of wands - inverted -  inner resources, struggle, overwhelm, defensive, paranoia."],
    ["|10w| - ten of wands - upright - burden, extra responsibility, hard work, completion.", "|10| - ten of wands - inverted - doing it all, carrying the burden, delegation, release."],
    ["|pw| - page of wands - upright -  inspiration, ideas, discovery, limitless potential, free spirit.", "|p| - page of wands - inverted - newly-formed ideas, redirecting energy, self-limiting beliefs, a spiritual path."],
    ["|jw| - jack of wands - upright - energy, passion, inspired action, adventure, impulsiveness.", "|j| - jack of wands - inverted -  passion project, haste, scattered energy, delays, frustration."],
    ["|kw| - king of wands - upright - vision, entrepreneur, honour.", "|k| - king of wands - inverted -  impulsiveness, haste, ruthless, high expectations."],
    ["|qw| - queen of wands - upright - courage, confidence, independence, social butterfly, determination.", "|q| - queen of wands - inverted - self-respect, self-confidence, introverted, re-establish sense of self."],
    ["|ac| - ace of cups - upright - love, new relationships, compassion, creativity.", "|a| - ace of cups - inverted - self-love, intuition, repressed emotions."],
    ["|2c| - two of cups - upright - unified love, partnership, mutual attraction", "|2| - two of cups - inverted - self-love, break-ups, disharmony, distrust."],
    ["|3c| - three of cups - upright - celebration, friendship, creativity, collaborations.", "|3| - three of cups - inverted - independence, alone time, hardcore partying, 'three's a crowd'."],
    ["|4c| - four of cups - upright - meditation, contemplation, apathy, re-evaluation.", "|4| - four of cups - inverted - retreat, withdrawal, checking in for alignment."],
    ["|5c| - five of cups - upright - regret, failure, disappointment, pessimism.", "|5| - five of cups - inverted - personal setbacks, self-forgiveness, moving on."],
    ["|6c| - six of cups - upright - revisiting the past, childhood memories, innocence, joy.", "|6| - six of cups - inverted - living in the past, forgiveness, lacking playfulness."],
    ["|7c| - seven of cups - upright - opportunities, choices, wishful thinking, illusion.", "|7| - seven of cups - inverted - alignment, personal values, overwhelmed by choices."],
    ["|8c| - eight of cups - upright - disappointment, abandonment, withdrawal, escapism.", "|8| - eight of cups - inverted - indecision, aimless drifting, walking away."],
    ["|9c| - nine of cups - upright - contentment, satisfaction, gratitude, wish come true.", "|9| - nine of cups - inverted - inner happiness, materialism, dissatisfaction, indulgence."],
    ["|10c| - ten of cups - upright - divine love, blissful relationships, harmony, alignment.", "|10| - ten of cups - inverted - disconnection, misaligned values, struggling relationships."],
    ["|pc| - page of cups - upright - creative opportunities, intuitive messages, curiosity, possibility.", "|p| - page of cups - inverted - new ideas, doubting intuition, creative blocks, emotional immaturity."],
    ["|jc| - jack of cups - upright - creativity, romance, charm, imagination, beauty.", "|j| - jack of cups - inverted - overactive imagination, unrealistic, jealous, moody."],
    ["|kc| - king of cups - upright - emotionally balanced, compassionate, diplomatic.", "|k| - king of cups - inverted - self-compassion, inner feelings, moodiness, emotionally manipulative."],
    ["|qc| - queen of cups - upright - compassionate, caring, emotionally stable, intuitive, in flow.", "|q| - queen of cups - inverted - inner feelings, self-care, self-love, co-dependency."],
]

ascii_past = """
  ___                ^    ______
 ||   \\    //\\     /   \\ <______>  
 || |) )  //__\\    | | |    ||
 ||___/  //____\\   \\  \\/    ||
 ||     //      \\  /\\  \\    ||
 ||    //        \\ | | |    ||
 ||   //          \\ \\ /     ||
"""

ascii_present = """
 ___      ____    _____    ^    _______             ________
||   \\  ||    \\ ||_____> /   \\  ||_____> ||\\\\    ||<________>
|| |) ) ||  |) )||       | | |  ||       || \\\\   ||    ||
||___/  ||____/ ||____   \\  \\/  ||____   ||  \\\\  ||    ||
||      ||\\\\    ||       /\\  \\  ||       ||   \\\\ ||    ||
||      || \\\\   ||_____  | | |  ||_____  ||    \\\\||    ||
||      ||  \\\\  ||_____>  \\ /   ||_____> ||      ||    ||
"""

ascii_future = """
 _______                             _____    _____
||______> ||   || <-------> ||   || ||    \\  ||____>
||        ||   ||     |     ||   || || |)  ) ||
||____    ||   ||     |     ||   || ||____/  ||___
||        ||   ||     |     ||   || ||\\\\     ||
||        ||___||     |     ||___|| || \\\\    ||_____
||        |_____|     |     |_____| ||  \\\\   ||_____>
"""

draw = random.sample(all_cards, 3)

k = random.randint(0, 1)
l = random.randint(0, 1)
m = random.randint(0, 1)

print(ascii_past)
print(draw[0][k])
print(ascii_present)
print(draw[1][l])
print(ascii_future)
print(draw[2][m])

