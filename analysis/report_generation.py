import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from jinja2 import Environment, FileSystemLoader
import pdfkit

def generate_report(analysis_results, username):
    report_path = f'reports/{username}_report.pdf'
    
    # Create visualizations
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=analysis_results, x='timestamp', y='likes', label='Likes')
    sns.lineplot(data=analysis_results, x='timestamp', y='comments', label='Comments')
    sns.lineplot(data=analysis_results, x='timestamp', y='recasts', label='Recasts')
    plt.title('Engagement Over Time')
    plt.xlabel('Time')
    plt.ylabel('Engagement')
    plt.legend()
    plt.savefig(f'static/{username}_engagement_over_time.png')
    plt.close()

    # Load template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report.html')

    # Render template
    html_out = template.render(username=username, img_path=f'static/{username}_engagement_over_time.png')
    
    # Generate PDF
    pdfkit.from_string(html_out, report_path)
    
    return report_path
