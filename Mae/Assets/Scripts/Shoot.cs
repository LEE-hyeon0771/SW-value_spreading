using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Shoot : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
          
    }
    private void OnTriggerEnter2D(Collider2D collision)
    {
        var hit = collision.gameObject.tag;
        if (hit == "Falcon" && GameManager.state == PlayState.Play)
        {
            PlayManager.r_cnt -= 1;
            collision.gameObject.SetActive(false);
        }
    }
}
