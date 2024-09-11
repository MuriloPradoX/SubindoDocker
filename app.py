from flask import Flask, render_template_string
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def grafico():
    plt.figure()
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plt.plot(x, y)



    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    
    graph_url = base64.b64encode(img.getvalue()).decode('utf8')
    img_tag = f'<img src="data:image/png;base64,{graph_url}"/>'


    return render_template_string(f'<h1>Gráfico Aula</h1>{img_tag}')




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
