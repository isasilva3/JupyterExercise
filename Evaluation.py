import seg_metrics.seg_metrics as sg
import SimpleITK as sitk

#labels_dir = '/home/imoreira/Segmentations/Pred'

#labels_dicts = [{"image": image_name} for image_name in zip(labels_dir)]





labels=[0,4,5,6,7,8]

metrics = sg.write_metrics(labels=labels[1:],
                            gdth_path='/home/imoreira/Metrics/Labels',
                            pred_path='/home/imoreira/Metrics/Pred',
                            csv_file='Metrics.csv',
                            metrics=['dice', 'hd'])


print(metrics)