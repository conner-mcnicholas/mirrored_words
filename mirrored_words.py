from collections import Counter
import pandas as pd
pd.set_option('display.max_rows', None)

# Open the file in append mode
with open('README.MD', 'a') as f:
    # Print to the file, ensuring each print adds a new line
    print("\n# GOAL\n\nThis script finds the instances where 2 words require the same keystrokes, except mirroring left and right hand responsibilities \
          \n\t(i.e. 'p' corresponds with 'q', 'f' corresponds with 'j', etc)\n\n", file=f)
    print("Results are compiled for each of the available English words lists from MonkeyType.com as input \
          \n\t(i.e. 200, 1k, 5k, 10k, 25k, 450k)", file=f)
    print("\n\n## RESULTS\n\n", file=f)

qwerty_mirror = {
    'q':'p','w':'o','e':'i','r':'u','t':'y',
            's':'l','d':'k','f':'j','g':'h',
                    'c':'m','v':'n', 
                                    'b':'b',
    'p':'q','o':'w','i':'e','u':'r','y':'t',
            'l':'s','k':'d','j':'f','h':'g',
                    'm':'c','n':'v'}

for i in ['200','1k','5k','10k','25k','450k']:
    # Load a dictionary file of words
    with open(rf"wordlists\\english_{i}.txt") as f:
        words = set(w.strip().lower() for w in f if w.strip().isalpha())

    mirrorlist = [["",""]]

    for w in words:
        if (set(w) & set("azx")):
            continue
        mir_w = "".join(qwerty_mirror[l] for l in w)
        if (mir_w in words) and not(w in [x[1] for x in mirrorlist]):
            #print(f"{mir_w} <-> {w}")
            mirrorlist.append([w,mir_w])

    df_mirror = pd.DataFrame(sorted(mirrorlist,key=lambda pair:(len(pair[0]),pair[0])),columns=['word','mirror'])[1:]
    df_mirror.to_csv(f"results\\mirror_pairs_{i}.csv",index=False)
    with open('README.md', 'a') as f:
        print(f"\nUsing wordlist --> English_{i}.txt\n", file=f)
        print(f"\ttotal # pairs: {len(df_mirror)}\n", file=f)
        if len(df_mirror) > 0:
            longest = df_mirror['word'].str.len().max()
            df_longest = df_mirror[df_mirror['word'].str.len() == longest]
            print(f"\tlongest:{longest}\n\t{[[df_longest['word'].iloc[x],df_longest['mirror'].iloc[x]] for x in range(len(df_longest))]}", file=f)
