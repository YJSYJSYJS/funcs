from pytube import YouTube
import argparse
import pickle

def main(args):
    link_form = 'https://www.youtube.com/watch?v='

    err_lists = list()

    with open(args.ids) as f:
        lines = f.readlines()
        total = len(lines)
        curr_idx = 0
        for l in lines:
            curr_idx+=1 # if not run on background, erase this line
            print('{}/{}'.format(curr_idx, total)) # if not run on background, erase this line
            if l[-2:]=='\n':
                fname = l[:-1]
            else:
                fname = l
            curr_link = link_form + fname
            try:
                yt = YouTube(curr_link)
                yt.streams.first().download(output_path=args.save, filename=fname)
            except:
                err_lists.append(l)
                continue
    
    with open(args.errs, 'wb') as f:
        pickle.dump(err_lists, f)
                
                
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ids', type=str, required=True, help='youtube ids txt file dir')
    parser.add_argument('--save', type=str, required=True, help='youtube video download dir')
    parser.add_argument('--errs', type=str, required=True, help='download failed ids')
    args = parser.parse_args()
    main(args)