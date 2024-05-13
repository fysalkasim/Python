alien_0 = {'X_position': 0, 'Y_position': 25, 'Speed':'medium'}
print(f"The inial location of alien is:{alien_0['X_position']},{alien_0['Y_position']}")
def sped():
    if alien_0['Speed'] == 'medium':
        alien_0['X_position'] += 2 
    elif alien_0['Speed'] == 'slow':
        alien_0['X_position'] += 1
    else:
        alien_0['X_position'] += 35
    print(f"The current position of alien is: {alien_0['X_position']},{alien_0['Y_position']}")


pace = input("Enter current speed for the alien: Slow/Medium/Fast")
alien_0['Speed'] = pace
pl = sped()
