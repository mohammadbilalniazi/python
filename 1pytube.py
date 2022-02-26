from flask import Flask,request,render_template
from pytube import YouTube
import tqdm,time

app=Flask(__name__)
 
@app.route("/download",methods=["POST","GET"])
def download():
     if request.method=="POST":
         url=request.form["url"]
         try:
             yt_obj = YouTube(url)
             filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
             for i in tqdm(filters.get_highest_resolution().download(), desc = 'Downloading in Progress'):
                  time.sleep(0.01)		
             #filters.get_highest_resolution().download()
             msg='Video Downloaded Successfully'
         except Exception as e:
             msg=e
             
         return 'ok'
     else:
         return render_template("download.html")


if __name__=="__main__":
    app.run(debug=True)
