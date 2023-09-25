import requests



import json
import time








async def softs_5(init, promts, scale, safety):
    
    
    s = {
    "key": "UdIXcJpmuLjV68h51zWdaPeGF5koIdM0hoyBkxClpQNPKGxZEqsCAUrFUzKb",
    
    "prompt": promts,
    
    "negative_prompt": "High pass filter, airbrush,portrait,zoomed, soft light, smooth skin,closeup, Anime, fake, cartoon, deformed, extra limbs, extra fingers, mutated hands, bad anatomy, bad proportions , blind, bad eyes, ugly eyes, dead eyes, blur, vignette, out of shot, out of focus, gaussian, closeup, monochrome, grainy, noisy, text, writing, watermark, logo, oversaturation , over saturation, over shadow, floating limbs, disconnected limbs, anime, kitsch, cartoon, penis, fake, (black and white), airbrush, drawing, illustration, boring, 3d render, long neck, out of frame, extra fingers, mutated hands, monochrome, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, glitchy, bokeh, (((long neck))), (child), (childlike), 3D, 3DCG, cgstation, red eyes, multiple subjects, extra heads, close up, man, ((asian)), text, bad anatomy, morphing, messy broken legs decay, ((simple background)), deformed body, lowres, bad anatomy, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low jpeg artifacts, signature, watermark, username, blurry, out of focus, old, amateur drawing, odd, fat, morphing, ((simple background)), artifacts, signature, artist name, [blurry], disfigured, mutated, (poorly hands), messy broken legs, decay, painting, duplicate, closeup",
  
    "model_id": "f222-diffusion",
    "init_image": init,
  
    
  
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "30",
    "safety_checker": safety,
    "enhance_prompt": "yes",
  
    
    "guidance_scale": scale,
    "strength": 0.7,
  
    
    
    
    
    "seed": None,
    "webhook": None,
    "track_id": None,
    
    "scheduler": "UniPCMultistepScheduler",
    "lora_model": None,
    "tomesd": "yes",
    "use_karras_sigmas": "yes",
    "vae": None,
    "lora_strength": None,
    "embeddings_model": None,
    "webhook": None,
    "track_id": None
    
    
    }

    datas = json.dumps(s)
    headers = {
    'Content-Type': 'application/json'
    }
    res = requests.post('https://stablediffusionapi.com/api/v4/dreambooth/img2img',headers=headers, data=datas)




    result = json.loads(res.text)
    
    print(result)
    
    if result.get('status') == 'processing':
        time.sleep(18)
        res_ = requests.post(f'{result.get("fetch_result")}',headers=headers, data=datas)
        res_5 = json.loads(res_.text)
        return res_5.get('output')[0]
    elif result.get('status') == 'error':
        return None
    else:
        return result.get('output')[0]




async def softstexts(promts,safety,scale):

    s = {
    "key": "UdIXcJpmuLjV68h51zWdaPeGF5koIdM0hoyBkxClpQNPKGxZEqsCAUrFUzKb",
    
    "prompt": promts,
    
    "negative_prompt": "High pass filter, airbrush,portrait,zoomed, soft light, smooth skin,closeup, Anime, fake, cartoon, deformed, extra limbs, extra fingers, mutated hands, bad anatomy, bad proportions , blind, bad eyes, ugly eyes, dead eyes, blur, vignette, out of shot, out of focus, gaussian, closeup, monochrome, grainy, noisy, text, writing, watermark, logo, oversaturation , over saturation, over shadow, floating limbs, disconnected limbs, anime, kitsch, cartoon, penis, fake, (black and white), airbrush, drawing, illustration, boring, 3d render, long neck, out of frame, extra fingers, mutated hands, monochrome, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, glitchy, bokeh, (((long neck))), (child), (childlike), 3D, 3DCG, cgstation, red eyes, multiple subjects, extra heads, close up, man, ((asian)), text, bad anatomy, morphing, messy broken legs decay, ((simple background)), deformed body, lowres, bad anatomy, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low jpeg artifacts, signature, watermark, username, blurry, out of focus, old, amateur drawing, odd, fat, morphing, ((simple background)), artifacts, signature, artist name, [blurry], disfigured, mutated, (poorly hands), messy broken legs, decay, painting, duplicate, closeup",
    "model_id": "f222-diffusion",
  
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "30",
    "safety_checker": safety,
    "enhance_prompt": "yes",
    "num_inference_steps": "30",
    "seed": None,
    "multi_lingual": "no",
    "panorama": "no",
    "self_attention": "no",
    "upscale": "no",
    "embeddings_model": None,
    "lora_model": None,
    "tomesd": "yes",
    "use_karras_sigmas": "yes",
    "vae": None,
    "lora_strength": None,
    "scheduler": "UniPCMultistepScheduler",
    "webhook": None,
    "track_id": None,
    "guidance_scale": scale

    }

    
    
    
    
    
    
    
    datas = json.dumps(s)
    headers = {
    'Content-Type': 'application/json'
    
    
    
    
    
    }
    res = requests.post('https://stablediffusionapi.com/api/v4/dreambooth',headers=headers, data=datas)

    result = json.loads(res.text)
    
    
    print(result)
    if result.get('status') == 'processing':
        time.sleep(18)
        res_ = requests.post(f'{result.get("fetch_result")}',headers=headers, data=datas)
        res_5 = json.loads(res_.text)
        return res_5.get('output')[0]
    elif result.get('status') == 'error':
        
        return None
    
    
    
    else:
        return result.get('output')[0]